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
#     spack install py-sigprofilerextractor
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilerextractor
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilerextractor(PythonPackage):
    """SigProfilerExtractor allows de novo extraction of mutational signatures from data generated in a matrix format. The tool identifies the number of operative mutational signatures, their activities in each sample, and the probability for each signature to cause a specific mutation type in a cancer sample. The tool makes use of SigProfilerMatrixGenerator and SigProfilerPlotting."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerExtractor"

    url = "https://github.com/AlexandrovLab/SigProfilerExtractor/archive/refs/tags/v1.1.24.tar.gz"

    license("BSD-2-Clause")

    version(
        "1.1.24",
        sha256="3a425839ef25c8b404ef99dabef42aea8215cf6edc6cb8f551a12b6c926fc628",
    )
    version(
        "1.1.23",
        sha256="8b112492f787fd3a74ae2fce43a95d64cd27a4082122b25e48c9d5adba9b121f",
    )
    version(
        "1.1.4",
        sha256="6fd012b6bc7e3c394353c2f229f8bf19648a7d6f2418f96e968f2ea8db2213c9",
    )
    version(
        "1.1", sha256="51eb7c04c4c5923d9d543c9d6804249fedb64758b5913d04bf5fa62eb26ba061"
    )

    depends_on("py-setuptools", type="build")
    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))
