# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuclimatch(RPackage):
	"""Euclidean Climatch Algorithm

	An interface for performing climate matching using the Euclidean "Climatch" algorithm. Functions provide a vector of climatch scores (0-10) for each location (i.e., grid cell) within the recipient region, the percent of climatch scores >= a threshold value, and mean climatch score. Tools for parallelization and visualizations are also provided. Note that the floor function that rounds the climatch score down to the nearest integer has been removed in this implementation and the “Climatch” algorithm, also referred to as the “Climate” algorithm, is described in: Crombie, J., Brown, L., Lizzio, J., & Hood, G. (2008). “Climatch user manual”. The method for the percent score is described in: Howeth, J.G., Gantz, C.A., Angermeier, P.L., Frimpong, E.A., Hoff, M.H., Keller, R.P., Mandrak, N.E., Marchetti, M.P., Olden, J.D., Romagosa, C.M., and Lodge, D.M. (2016). <doi:10.1111/ddi.12391>.
	"""
	
	cran = "Euclimatch" 

	version("1.0.1", md5="72264f3b624e64fc84eb7de740658e3f")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-rcppparallel", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
