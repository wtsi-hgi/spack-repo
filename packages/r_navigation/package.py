# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNavigation(RPackage):
	"""Analyze the Impact of Sensor Error Modelling on Navigation
Performance

	Implements the framework presented in Cucci, D. A., Voirol, L., Khaghani, M. and Guerrier, S. (2023) <doi:10.1109/TIM.2023.3267360> which allows to analyze the impact of sensor error modeling on the performance of integrated navigation (sensor fusion) based on inertial measurement unit (IMU), Global Positioning System (GPS), and barometer data.
             The framework relies on Monte Carlo simulations in which a Vanilla Extended Kalman filter is coupled with realistic and user-configurable noise generation mechanisms to recover a reference trajectory from noisy measurements. 
             The evaluation of several statistical metrics of the solution, aggregated over hundreds of simulated realizations, provides reasonable estimates of the expected performances of the system in real-world conditions.
	"""
	
	homepage = "https://github.com/SMAC-Group/navigation"
	cran = "navigation" 

	version("0.0.1", md5="ba4179001331466fdbb66be35224285b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-simts", type=("build", "run"))
	depends_on("r-expm", type=("build", "run"))
	depends_on("r-rbenchmark", type=("build", "run"))
	depends_on("r-leaflet", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
