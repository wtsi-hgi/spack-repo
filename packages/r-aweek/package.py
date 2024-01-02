# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *

class RAweek(RPackage):
    """Which day a week starts depends heavily on the either the local or professional context."""

    homepage = "https://www.repidemicsconsortium.org/aweek/"
    cran = "aweek"

    version("1.0.3", sha256="9a3be230985b98d36f697185d7832261407c2c6fbf2d6089ab09e59755edc192")
    version("1.0.2", sha256="84d6a890827326efd54b98202abd831ef701ebea27bd817d4abfd79c80737f02")
    version("1.0.1", sha256="be087cd860af73ba8090f4813bd793700cb94a14883365d52ca684870700567c")
    version("1.0.0", sha256="894b0563e4761caca8df66aac06b824158cd5d61180157c9800c9364ae272d29")
    version("0.2.2", sha256="a0e617e17843d64db1ca084ce56e63bf346a302dfe7154d823b4add2fe777f44")
    version("0.2.0", sha256="4bfa91fdf12e435ca518ae2f4ed2bcf3d0e0ce7d96a413ce5468a006db1870f3")
    version("0.1.0", sha256="69347f94a3472bc449da429bf6601aeacf7590e99ccc762a4a88ffef5eca04f3")

    depends_on("r-testthat", type=("build", "run"))
    depends_on("r-roxygen2", type=("build", "run"))
    depends_on("r-knitr", type=("build", "run"))
    depends_on("r-rmarkdown", type=("build", "run"))
    depends_on("r-covr", type=("build", "run"))
    depends_on("r-spelling", type=("build", "run"))
