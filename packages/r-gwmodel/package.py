# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGwmodel(RPackage):
	"""Geographically-Weighted Models.

	Techniques from a particular branch of spatial statistics,termed
	geographically-weighted (GW) models. GW models suit situations when data
	are not described well by some global model, but where there are spatial
	regions where a suitably localised calibration provides a better
	description. 'GWmodel' includes functions to calibrate: GW summary
	statistics (Brunsdon et al., 2002) <doi:10.1016/s0198-9715(01)00009-6>, GW
	principal components analysis (Harris et al., 2011)
	<doi:10.1080/13658816.2011.554838>, GW discriminant analysis (Brunsdon et
	al., 2007) <doi:10.1111/j.1538-4632.2007.00709.x> and various forms of GW
	regression (Brunsdon et al., 1996)
	<doi:10.1111/j.1538-4632.1996.tb00936.x>; some of which are provided in
	basic and robust (outlier resistant) forms."""

	cran = "GWmodel"

	version("2.3-2", md5="2ec7200589386b6109fd6474696bf0f4")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-sp@1.4.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-spacetime", type=("build", "run"))
	depends_on("r-spdep", type=("build", "run"))
	depends_on("r-spatialreg", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
