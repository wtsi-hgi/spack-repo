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
#     spack install py-sigprofilersimulator
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilersimulator
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilersimulator(PythonPackage):
    """SigProfilerSimulator allows realistic simulations of mutational signatures in cancer genomes. The tool can be used to simulate signatures of single point mutations, double point mutations, and insertion/deletions. Further, the tool makes use of SigProfilerMatrixGenerator and SigProfilerPlotting."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerSimulator"

    url = "https://github.com/AlexandrovLab/SigProfilerSimulator/archive/refs/tags/v1.1.6.tar.gz"

    license("BSD-2-Clause")

    version(
        "1.1.6",
        sha256="799ecd3b3b05561c73d2ba85efcd84b4c14691d7611c7a1aa341f95c7284aac3",
    )
    version(
        "1.1.5",
        sha256="367de5d448a1b3a0209e8661eb52e3548d20bcd5c815bc83d534b8f45c9acb27",
    )
    version(
        "1.1", sha256="eab83024f63756a7022b1d651996c380e3f7258725c6d12cd230934488cea67e"
    )
    version(
        "1.0", sha256="783129fb576a512b241bbbca3906596d0856f0813b9e869669de7e9f3a02ab31"
    )

    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))

    depends_on("py-setuptools", type="build")
