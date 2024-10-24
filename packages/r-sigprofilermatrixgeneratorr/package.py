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
#     spack install r-sigprofilermatrixgeneratorr
#
# You can edit this file again by typing:
#
#     spack edit r-sigprofilermatrixgeneratorr
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class RSigprofilermatrixgeneratorr(RPackage):
    """An R wrapper for running the SigProfilerMatrixGenerator framework."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerMatrixGeneratorR"
    url = "https://github.com/AlexandrovLab/SigProfilerMatrixGeneratorR/archive/refs/tags/v1.2.tar.gz"

    license("BSD-2-Clause")

    version(
        "1.2", sha256="91854a696ea827974b085f05a3492298ac3ac90fcd9a33d48d2756a143728ba0"
    )
    version(
        "1.1", sha256="231d9cd416787edebcd880075fbb981ead9e3be9ee70e0e7f74b61628a10c171"
    )
    version(
        "1.0", sha256="bad5738e5bd477fffe9f3a20df84c49387797cd10afbad17491630bb407c48b2"
    )

    depends_on("python@3.8:", type=("build", "run"))
    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-devtools", type=("build", "run"))
