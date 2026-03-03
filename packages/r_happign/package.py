# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHappign(RPackage):
	"""R Interface to 'IGN' Web Services

	Automatic open data acquisition from resources of IGN
    ('Institut National de Information Geographique et forestiere')
    (<https://www.ign.fr/>). Available datasets include various types of
    raster and vector data, such as digital elevation models, state
    borders, spatial databases, cadastral parcels, and more. There also
    access to point clouds data ('LIDAR') and specifics API
    (<https://apicarto.ign.fr/api/doc/>).
	"""
	
	homepage = "https://github.com/paul-carteron"
	cran = "happign" 

	version("0.2.2", md5="ff041b51edfb6bcaeee9d18ca9bf73c9")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-archive", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-httr2", type=("build", "run"))
	depends_on("r-sf@1.0.7:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-units", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("gdal@2.0.1:", type=("build", "link", "run"))
	depends_on("geos@3.4.0:", type=("build", "link", "run"))
	depends_on("proj@4.8.0:", type=("build", "link", "run"))
	depends_on("sqlite@3:", type=("build", "link", "run"))
