from fileformats.generic import File


class Head(File):
    ext = ".HEAD"
    binary = True


class All1(File):
    ext = ".all1"
    binary = True


class OneD(File):
    ext = ".1D"
    binary = True


class R1(File):
    ext = ".r1"
    binary = True


class ThreeD(File):
    ext = ".3D"
    binary = True
    alternate_exts = (".3d",)


class Dset(File):
    ext = ".dset"
    binary = True
