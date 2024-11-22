# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install king
#
# You can edit this file again by typing:
#
#     spack edit king
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

import glob

from spack.package import *


class King(Package):
    """KING (Kinship-based INference for Gwas) is a toolset that makes use of high-throughput SNP data typically seen in a genome-wide association study (GWAS) or a sequencing project. Applications of KING include family relationship inference and pedigree error checking, quality control, population substructure identification, forensics, gene mapping, etc."""

    homepage = "https://kingrelatedness.com/"
    url = "https://www.kingrelatedness.com/executables/KING2.3.2code.tar.gz"

    version("2.3.2", md5="f0c9bf64a16c75c523b8f62f56d14260")

    depends_on("gcc", type="build")
    depends_on("zlib-api")
    depends_on("lapack")
    depends_on("r", type=("build", "run"))
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-e1071", type=("build", "run"))

    patch("rplot.patch")

    def install(self, spec, prefix):
        mkdirp(prefix.bin)
        which("g++")(
            "-lm",
            "-lz",
            "-DWITH_LAPACK=1",
            *spec["lapack"].libs.ld_flags.split(),
            "-I" + spec["lapack"].prefix.include,
            "-I" + spec["zlib-api"].prefix.include,
            "-L" + spec["zlib-api"].prefix.lib,
            "-O2",
            "-fopenmp",
            "-o",
            f"{prefix.bin}/king",
            *glob.glob("*.cpp"),
        )
