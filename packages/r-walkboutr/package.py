# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWalkboutr(RPackage):
	"""Generate Walk Bouts from GPS and Accelerometry Data

	Process GPS and accelerometry data to generate walk bouts. A walk bout is a period of activity with accelerometer movement matching the patterns of walking with corresponding GPS measurements that confirm travel. The inputs of the 'walkboutr' package are individual-level accelerometry and GPS data. The outputs of the model are walk bouts with corresponding times, duration, and summary statistics on the sample population, which collapse all personally identifying information. These bouts can be used to measure walking both as an outcome of a change to the built environment or as a predictor of health outcomes such as a cardioprotective behavior. Kang B, Moudon AV, Hurvitz PM, Saelens BE (2017) <doi:10.1016/j.trd.2017.09.026>.
	"""
	
	homepage = "https://github.com/rwalkbout/walkboutr"
	cran = "walkboutr" 

	version("0.6.0", md5="8386a3709bed04e35c6f34301945d711")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-geosphere", type=("build", "run"))
	depends_on("r-ggforce", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-lwgeom", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-measurements", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
