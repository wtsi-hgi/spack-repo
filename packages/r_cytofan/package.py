# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCytofan(RPackage):
	"""Plot Fan Plots for Cytometry Data using 'ggplot2'

	An implementation of Fan plots for cytometry data in 'ggplot2'. 
    For reference see Britton, E.; Fisher, P. & J. Whitley (1998) The Inflation Report Projections: Understanding the Fan Chart 
    <https://www.bankofengland.co.uk/quarterly-bulletin/1998/q1/the-inflation-report-projections-understanding-the-fan-chart>).
	"""
	
	homepage = "https://github.com/yannabraham/cytofan"
	cran = "cytofan" 

	version("0.1.0", md5="044cfe718216d2a5dbad87a7a18cd0c1")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ggplot2@2.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
