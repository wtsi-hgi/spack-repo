# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransfr(RPackage):
	"""Transfer of Hydrograph from Gauged to Ungauged Catchments

	A geomorphology-based hydrological modelling for transferring
    streamflow measurements from gauged to ungauged catchments. Inverse
    modelling enables to estimate net rainfall from streamflow measurements 
    following Boudhraâ et al. (2018) <doi:10.1080/02626667.2018.1425801>. 
    Resulting net rainfall is then estimated on the ungauged catchments 
    by spatial interpolation in order to finally simulate streamflow 
    following de Lavenne et al. (2016) <doi:10.1002/2016WR018716>.
	"""
	
	homepage = "https://gitlab.irstea.fr/HYCAR-Hydro/transfr"
	cran = "transfR" 

	version("1.0.11", md5="57086c84470d50098dc573c96afd3310")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-stars@0.4.0:", type=("build", "run"))
	depends_on("r-sf@0.8.0:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
