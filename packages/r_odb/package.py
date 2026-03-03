# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROdb(RPackage):
	"""Open Document Databases (.odb) Management

	Functions to create, connect, update and query 'HSQL' databases embedded in Open Document Databases files, as 'OpenOffice' and 'LibreOffice' do.
	"""
	
	homepage = "http://bioinformatics.ovsa.fr/ODB"
	cran = "ODB" 

	version("1.2.1", md5="ad9bd579f32aa793d9122ffed6342630")

	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-rjdbc", type=("build", "run"))
	depends_on("zip", type=("build", "link", "run"))
