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
#     spack install py-sigprofilersinglesample
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilersinglesample
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilersinglesample(PythonPackage):
    """SigProfilerSingleSample allows attributing a known set of mutational signatures to an individual sample. The tool identifies the activity of each signature in the sample and assigns the probability for each signature to cause a specific mutation type in the sample. The tool makes use of SigProfilerMatrixGenerator, SigProfilerExtractor and SigProfilerPlotting."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerSingleSample"
    git = "https://github.com/AlexandrovLab/SigProfilerSingleSample.git"

    license("BSD-2-Clause")

    version("20201209", commit="37922459ca2d5696f598ac2b9d109ca3543f24bf")

    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))
    depends_on("py-sigprofilerextractor", type=("build", "run"))
