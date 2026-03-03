# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatapack(RPackage):
	"""A Flexible Container to Transport and Manipulate Data and
Associated Resources

	Provides a flexible container to transport and manipulate complex
    sets of data. These data may consist of multiple data files and associated
    meta data and ancillary files. Individual data objects have associated system
    level meta data, and data files are linked together using the OAI-ORE standard
    resource map which describes the relationships between the files. The OAI-
    ORE standard is described at <https://www.openarchives.org/ore/>. Data packages
    can be serialized and transported as structured files that have been created
    following the BagIt specification. The BagIt specification is described at
    <https://tools.ietf.org/html/draft-kunze-bagit-08>.
	"""
	
	homepage = "https://docs.ropensci.org/datapack/"
	cran = "datapack" 

	version("1.4.1", md5="e4fd89576331a3ba2fdf95c9dcb5468f")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-fs", type=("build", "run"))
	depends_on("r-redland", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-uuid", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
