def daemonize(preserve_fds=None):
    """Standard daemonization of a process.
    http://www.svbug.com/documentation/comp.unix.programmer-FAQ/faq_2.html#SEC16
    
    source: https://github.com/progrium/ginkgo/blob/master/ginkgo/util.py
    """
    def _maxfd(limit=1024):
        maxfd = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
        if maxfd == resource.RLIM_INFINITY:
            return limit
        else:
            return maxfd

    def _devnull(default="/dev/null"):
        if hasattr(os, "devnull"):
            return os.devnull
        else:
            return default

    def _close_fds(preserve=None):
        preserve = preserve or []
        for fd in xrange(0, _maxfd()):
            if fd not in preserve:
                try:
                    os.close(fd)
                except OSError: # fd wasn't open to begin with (ignored)
                    pass

    if os.fork():
        os._exit(0)
    os.setsid()

    if os.fork():
        os._exit(0)

    os.umask(0)
    _close_fds(preserve_fds)

    os.open(_devnull(), os.O_RDWR)
    os.dup2(0, 1)
    os.dup2(0, 2)
