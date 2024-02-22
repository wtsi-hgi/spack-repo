# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RErtg3d(RPackage):
	"""Empirically Informed Random Trajectory Generation in 3-D

	Creates realistic random trajectories in a 3-D space between two given fix points, so-called conditional empirical random walks (CERWs). The trajectory generation is based on empirical distribution functions extracted from observed trajectories (training data) and thus reflects the geometrical movement characteristics of the mover. A digital elevation model (DEM), representing the Earth's surface, and a background layer of probabilities (e.g. food sources, uplift potential, waterbodies, etc.) can be used to influence the trajectories.
    Unterfinger M (2018). "3-D Trajectory Simulation in Movement Ecology: Conditional Empirical Random Walk". Master's thesis, University of Zurich. <https://www.geo.uzh.ch/dam/jcr:6194e41e-055c-4635-9807-53c5a54a3be7/MasterThesis_Unterfinger_2018.pdf>.
    Technitis G, Weibel R, Kranstauber B, Safi K (2016). "An algorithm for empirically informed random trajectory generation between two endpoints". GIScience 2016: Ninth International Conference on Geographic Information Science, 9, online. <doi:10.5167/uzh-130652>.
	"""
	
	homepage = "https://munterfi.github.io/eRTG3D/"
	cran = "eRTG3D" 

	version("0.7.0", md5="0e41ebbbb7d3c6dc7c461eb435f1a26a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circstats@0.2.6:", type=("build", "run"))
	depends_on("r-ggplot2@3.1.1:", type=("build", "run"))
	depends_on("r-pbapply@1.4.1:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
	depends_on("r-raster@2.9.5:", type=("build", "run"))
	depends_on("r-rastervis@0.45:", type=("build", "run"))
	depends_on("r-tiff@0.1.5:", type=("build", "run"))
