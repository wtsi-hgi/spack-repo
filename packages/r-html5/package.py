# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHtml5(RPackage):
	"""Creates Valid HTML5 Strings

	Generates valid HTML tag strings for HTML5 elements documented by Mozilla. 
    Attributes are passed as named lists, with names being the attribute name and values being the attribute value. 
    Attribute values are automatically double-quoted. To declare a DOCTYPE, wrap html() with function doctype().
    Mozilla's documentation for HTML5 is available here: <https://developer.mozilla.org/en-US/docs/Web/HTML/Element>.
    Elements marked as obsolete are not included. 
	"""
	
	cran = "html5" 

	version("1.0.2", md5="7c550fc61cc3902514b9357ed3d83ac0", url="https://cran.r-project.org/src/contrib/html5_1.0.2.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
