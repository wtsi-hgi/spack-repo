# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RShadowr(RPackage):
	"""Selenium Plugin to Manage Multi Level Shadow Elements on Web
Page

	Shadow Document Object Model is a web standard that offers component style and markup encapsulation. 
  It is a critically important piece of the Web Components story as it ensures that a component will work in any environment even if other CSS or JavaScript is at play on the page.
  Custom HTML tags can't be directly identified with selenium tools, because Selenium doesn't provide any way to deal with shadow elements. 
  Using this plugin you can handle any custom HTML tags.
	"""
	
	homepage = "https://github.com/ricilandolt/shadowr"
	cran = "shadowr" 

	version("0.0.2", md5="6f80866b6e8ceed7386ec29e85c29a0f")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rselenium@1.7.7:", type=("build", "run"))
