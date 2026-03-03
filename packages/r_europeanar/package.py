# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REuropeanar(RPackage):
	"""Interact with Metadata Records and Media on the Europeana
Repository

	Interact with the Europeana Data Model via a variety of API
 endpoints that contains digital collections from thousands of institutions
 around Europe. This translates to millions of Cultural Heritage Objects in the
 form of image, text, video, sound and 3D, accompanied by rich metadata. The
 Data Model design principles are based on the core principles and best
 practices of the Semantic Web and Linked Data efforts to which Europeana
 contributes (see, e.g., Doerr, Martin, et al. The europeana data model (edm).
 World Library and Information Congress: 76th IFLA general conference
 and assembly. Vol. 10. 2010.). The package also provides methods for bulk
 downloads of specific subsets of items, including both their metadata
 and their associated media files.
	"""
	
	homepage = "https://github.com/AleKoure/europeanaR"
	cran = "europeanaR" 

	version("0.1.0", md5="d830f9b69f7092985f5a7909b49d61cc")

	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
