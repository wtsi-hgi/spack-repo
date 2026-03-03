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
#     spack install py-sigprofilertopography
#
# You can edit this file again by typing:
#
#     spack edit py-sigprofilertopography
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack.package import *


class PySigprofilertopography(PythonPackage):
    """SigProfilerTopography allows evaluating the effect of chromatin organization, histone modifications, transcription factor binding, DNA replication, and DNA transcription on the activities of different mutational processes. SigProfilerTopography elucidates the unique topographical characteristics of mutational signatures. The tool seamlessly integrates with other SigProfiler tools including SigProfilerMatrixGenerator, SigProfilerSimulator, and SigProfilerAssignment."""

    homepage = "https://github.com/AlexandrovLab/SigProfilerTopography"
    git = "https://github.com/AlexandrovLab/SigProfilerTopography.git"

    license("BSD-2-Clause")

    version("1.0.98", commit="074e7ca9bcfde7c0935bd7d674a1f1088e29b409")

    depends_on("py-sigprofilermatrixgenerator", type=("build", "run"))
    depends_on("py-sigprofilersimulator", type=("build", "run"))
    depends_on("py-sigprofilerassignment", type=("build", "run"))
