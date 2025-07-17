# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTargetsearch(RPackage):
    """A package for the analysis of GC-MS metabolite profiling data

    This packages provides a flexible, fast and accurate method for targeted pre-processing of GC-MS data. The user provides a (often very large) set of GC chromatograms and a metabolite library of targets. The package will automatically search those targets in the chromatograms resulting in a data matrix that can be used for further data analysis.
    """

    homepage = "https://github.com/acinostroza/TargetSearch"
    bioc = "TargetSearch"

    version("2.10.0", commit="1a62936a14741b0d7956a83ad4b7c4e7488b6f84")
    version("2.4.2", commit="61967f1d3332665524e6d03d6158aeeb35f97a1e")

    depends_on("r-ncdf4", type=("build", "run"))
    depends_on("r-assertthat", type=("build", "run"))
