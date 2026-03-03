# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultimorbidity(RPackage):
	"""Harmonizing Various Comorbidity, Multimorbidity, and Frailty
Measures

	Identifying comorbidities, frailty, and multimorbidity in claims 
    and administrative data is often a duplicative process.
    The functions contained in this package are meant to first prepare the data to a format
    acceptable by all other packages, then provide a uniform and simple approach to
    generate comorbidity and multimorbidity metrics based on these claims data. The package
    is ever evolving to include new metrics, and is always looking for new measures to include.
    The citations used in this package include the following publications: 
    Anne Elixhauser, Claudia Steiner, D. Robert Harris, Rosanna M. Coffey (1998) <doi:10.1097/00005650-199801000-00004>,
    Brian J Moore, Susan White, Raynard Washington, et al. (2017) <doi:10.1097/MLR.0000000000000735>,
    Mary E. Charlson, Peter Pompei, Kathy L. Ales, C. Ronald MacKenzie (1987) <doi:10.1016/0021-9681(87)90171-8>,
    Richard A. Deyo, Daniel C. Cherkin, Marcia A. Ciol (1992) <doi:10.1016/0895-4356(92)90133-8>,
    Hude Quan, Vijaya Sundararajan, Patricia Halfon, et al. (2005) <doi:10.1097/01.mlr.0000182534.19832.83>,
    Dae Hyun Kim, Sebastian Schneeweiss, Robert J Glynn, et al. (2018) <doi:10.1093/gerona/glx229>,
    Melissa Y Wei, David Ratz, Kenneth J Mukamal (2020) <doi:10.1111/jgs.16310>,
    Kathryn Nicholson, Amanda L. Terry, Martin Fortin, et al. (2015) <doi:10.15256/joc.2015.5.61>,
    Martin Fortin, José Almirall, and Kathryn Nicholson (2017)<doi:10.15256/joc.2017.7.122>.
	"""
	
	homepage = "https://github.com/WYATTBENSKEN/multimorbidity"
	cran = "multimorbidity" 

	version("0.5.1", md5="202c51b88c2c8e0bc8398e816c6d9786")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sqldf", type=("build", "run"))
