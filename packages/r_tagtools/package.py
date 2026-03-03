# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTagtools(RPackage):
	"""Work with Data from High-Resolution Biologging Tags

	High-resolution movement-sensor tags typically include accelerometers 
    to measure body posture and sudden movements or changes in speed, 
    magnetometers to measure direction of travel, and pressure sensors
    to measure dive depth in aquatic or marine animals. The sensors in these tags usually sample many times per second. Some tags include sensors for speed, turning rate (gyroscopes), and sound. This package provides software tools to facilitate calibration, processing, and analysis of such data. Tools are provided for: data import/export; 
    calibration (from raw data to calibrated data in scientific units); 
    visualization (for example, multi-panel time-series plots); 
    data processing (such as event detection, calculation of derived metrics like jerk and 
    dynamic acceleration, dive detection, and dive parameter calculation); and statistical analysis (for example, track reconstruction, a rotation test, and Mahalanobis distance analysis).
	"""
	
	homepage = "<https://animaltags.org>"
	cran = "tagtools" 

	version("0.1.0", md5="b5df8ff18679ee52434dc4473fe94f6a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-circstats", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-latex2exp", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-matlab", type=("build", "run"))
	depends_on("r-ncdf4", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-signal", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-zoom", type=("build", "run"))
