# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWaywiser(RPackage):
	"""Ergonomic Methods for Assessing Spatial Models

	Assessing predictive models of spatial data can be
    challenging, both because these models are typically built for
    extrapolating outside the original region represented by training data
    and due to potential spatially structured errors, with "hot spots" of
    higher than expected error clustered geographically due to spatial
    structure in the underlying data. Methods are provided for assessing
    models fit to spatial data, including approaches for measuring the
    spatial structure of model errors, assessing model predictions at
    multiple spatial scales, and evaluating where predictions can be made
    safely. Methods are particularly useful for models fit using the
    'tidymodels' framework. Methods include Moran's I ('Moran' (1950)
    <doi:10.2307/2332142>), Geary's C ('Geary' (1954)
    <doi:10.2307/2986645>), Getis-Ord's G ('Ord' and 'Getis' (1995)
    <doi:10.1111/j.1538-4632.1995.tb00912.x>), agreement coefficients from
    'Ji' and Gallo (2006) (<doi: 10.14358/PERS.72.7.823>), agreement
    metrics from 'Willmott' (1981) (<doi: 10.1080/02723646.1981.10642213>)
    and 'Willmott' 'et' 'al'. (2012) (<doi: 10.1002/joc.2419>), an
    implementation of the area of applicability methodology from 'Meyer'
    and 'Pebesma' (2021) (<doi:10.1111/2041-210X.13650>), and an
    implementation of multi-scale assessment as described in 'Riemann'
    'et' 'al'. (2010) (<doi:10.1016/j.rse.2010.05.010>).
	"""
	
	homepage = "https://github.com/ropensci/waywiser"
	cran = "waywiser" 

	version("0.5.1", md5="91d3448c9ff22be7ebaf0de0293f52ce")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr@1.1:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-fnn", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-hardhat", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang@1.1:", type=("build", "run"))
	depends_on("r-sf@1.0.0:", type=("build", "run"))
	depends_on("r-spdep@1.1.9:", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-vctrs", type=("build", "run"))
	depends_on("r-yardstick@1.2:", type=("build", "run"))
