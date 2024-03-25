from ._version import __version__  # noqa: F401
from pathlib import Path
import typing as ty
from random import Random
from fileformats.core import FileSet, SampleFileGenerator
from fileformats.medimage_afni import (
    OneD,
    Dset,
    Head,
    All1,
    R1,
    ThreeD,
    NCorr,
)


@FileSet.generate_sample_data.register
def gen_sample_oned_data(
    oned: OneD,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_head_data(
    head: Head,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_all1_data(
    all1: All1,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_r1_data(
    r1: R1,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_threed_data(
    threed: ThreeD,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


@FileSet.generate_sample_data.register
def gen_sample_dset_data(
    dset: Dset,
    generator: SampleFileGenerator,
) -> ty.Iterable[Path]:
    raise NotImplementedError


def gen_sample_ncorr_data(
    ncorr: NCorr, dest_dir: Path, seed: ty.Union[int, Random], stem: ty.Optional[str]
):
    raise NotImplementedError
