import cProfile

def profile_this(fn):
    def profiled_fn(*args, **kwargs):
        fpath = fn.__name__+ '.profile'
        prof = cProfile.Profile()
        ret = prof.runcall(fn,*args,**kwargs)
        prof.dump_stats(fpath)
        return ret
    return profiled_fn

