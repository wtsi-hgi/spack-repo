# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmpbam(RPackage):
    """C++ Library for OpenMP-based multi-threaded sequential profiling of Binary Alignment Map (BAM) files

    This packages provides C++ header files for developers wishing to create R packages that processes BAM files. ompBAM automates file access, memory management, and handling of multiple threads 'behind the scenes', so developers can focus on creating domain-specific functionality. The included vignette contains detailed documentation of this API, including quick-start instructions to create a new ompBAM-based package, and step-by-step explanation of the functionality behind the example packaged included within ompBAM.
    """

    homepage = "https://github.com/alexchwong/ompBAM"
    bioc = "ompBAM"

    version("1.12.0", commit="a51bfde1a191b60c04c581415590f28194b9603d")
    version("1.6.0", commit="e27fbbb3817e29967b8f8cc0b76990c040907611")

    depends_on("r-rcpp", type=("build", "run"))
    depends_on("r-zlibbioc", type=("build", "run"))
