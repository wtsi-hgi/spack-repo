# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAirgrdatasets(RPackage):
	"""Hydro-Meteorological Catchments Datasets for the 'airGR'
Packages

	Sample of hydro-meteorological datasets extracted from the 'CAMELS-FR' French database <https://hal.inrae.fr/hal-03687235>. It provides metadata and catchment-scale aggregated hydro-meteorological time series on a pool of French catchments for use by the 'airGR' packages. 
	"""
	
	homepage = "https://gitlab.irstea.fr/HYCAR-Hydro/airgrgalaxy/airgrdatasets"
	cran = "airGRdatasets" 

	version("0.2.1", md5="f599466aa94c991358c8467f60ee3399")

	depends_on("r@3.5:", type=("build", "run"))
