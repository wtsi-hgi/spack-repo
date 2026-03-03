# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNordklimdata1(RPackage):
	"""Dataset for Climate Analysis with Data from the Nordic Region

	The Nordklim dataset 1.0 is a unique and useful achievement for climate 
    analysis. It includes observations of twelve different climate elements from 
    more than 100 stations in the Nordic region, in time span over 100 years.
    The project contractors were NORDKLIM/NORDMET on behalf of the National 
    meteorological services in Denmark (DMI), Finland (FMI), Iceland (VI), 
    Norway (DNMI) and Sweden (SMHI).
	"""
	
	cran = "nordklimdata1" 

	version("1.2", md5="ac7ce887c66ab9e69e20a0daee5069af", url="https://cran.r-project.org/src/contrib/nordklimdata1_1.2.tar.gz")

	depends_on("r@2.10:", type=("build", "run"))
