# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUpdateobject(RPackage):
	"""Find/fix old serialized S4 instances

	A set of tools built around updateObject() to work with old serialized S4 instances. The package is primarily useful to package maintainers who want to update the serialized S4 instances included in their package. This is still work-in-progress.
	"""
	
	homepage = "https://bioconductor.org/packages/updateObject"
	bioc = "updateObject" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/updateObject_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/updateObject/updateObject_1.6.0.tar.gz"]

	version("1.12.0", tag="RELEASE_3_21")
	version("1.6.0", sha256="aaf3864680f6405523a92ecef102842f6192028c53279d63c7e34ee922ca2b28")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocgenerics@0.47.1:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("git", type=("build", "link", "run"))
