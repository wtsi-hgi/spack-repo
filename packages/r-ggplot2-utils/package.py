# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgplot2Utils(RPackage):
	"""Selected Utilities Extending 'ggplot2'

	Selected utilities, in particular 'geoms' and 'stats'
    functions, extending the 'ggplot2' package. This package imports
    functions from 'EnvStats' <doi:10.1007/978-1-4614-8456-1> by Millard (2013), 
    'ggpp' <https://CRAN.R-project.org/package=ggpp> by Aphalo et al. (2023) 
    and 'ggstats' <doi:10.5281/zenodo.10183964> by Larmarange (2023), 
    and then exports them. This package also contains modified code from 
    'ggquickeda' <https://CRAN.R-project.org/package=ggquickeda> by 
    Mouksassi et al. (2023) for Kaplan-Meier lines and ticks additions to plots.  
    All functions are tested to make sure that they work reliably.
	"""
	
	homepage = "https://insightsengineering.github.io/ggplot2.utils/"
	cran = "ggplot2.utils" 

	version("0.3.1", md5="15d1c3e2cf63121a2ca44bfc311e667a")

	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-envstats", type=("build", "run"))
	depends_on("r-ggpp", type=("build", "run"))
	depends_on("r-ggstats", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
