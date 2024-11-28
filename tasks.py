from invoke import task


@task
def compress_lib(c):
    c.run("tar cfJ lib.tar.xz lib/src lib/build.zig lib/build.zig.zon")
