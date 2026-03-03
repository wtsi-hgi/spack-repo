# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMapspain(RPackage):
	"""Administrative Boundaries of Spain

	Administrative Boundaries of Spain at several levels
    (Autonomous Communities, Provinces, Municipalities) based on the
    'GISCO' 'Eurostat' database <https://ec.europa.eu/eurostat/web/gisco>
    and 'CartoBase SIANE' from 'Instituto Geografico Nacional'
    <https://www.ign.es/>.  It also provides a 'leaflet' plugin and the
    ability of downloading and processing static tiles.
	"""
	
	homepage = "https://ropenspain.github.io/mapSpain/"
	cran = "mapSpain" 

	version("0.9.0", md5="ec9a29f545b319bd20effffcc861c393")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-countrycode@1.2:", type=("build", "run"))
	depends_on("r-giscor@0.2.4:", type=("build", "run"))
	depends_on("r-rappdirs@0.3:", type=("build", "run"))
	depends_on("r-sf@0.9:", type=("build", "run"))
