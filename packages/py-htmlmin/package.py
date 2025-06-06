# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyHtmlmin(PythonPackage):
	"""An HTML Minifier"""
	
	homepage = "https://htmlmin.readthedocs.io/en/latest/"
	pypi = "htmlmin/htmlmin-0.1.6.tar.gz" 

	version("0.1.1", sha256="f32d654d851f3b27ce23cd66ef8d043962c2e7e831a09ea3b5918d4c10698e51")
	version("0.1.10", sha256="ca5c5dfbb0fa58562e5cbc8dc026047f6cb431d4333504b11853853be448aa63")
	version("0.1.11", sha256="f27fb96fdddeb1725ee077be532c7bea23288c69d0e996e7798f24fae7a14e5e")
	version("0.1.12", sha256="50c1ef4630374a5d723900096a961cff426dff46b48f34d194a81bbe14eca178")
	version("0.1.2", sha256="a8a6bebe98023feb71bda3e4b1762ec8b7b1719fb5082dbfc1cccaafbc4c3d28")
	version("0.1.3", sha256="4341875d311ad72fb703711f6aeb2966c423c01950e7dbb85bdd7f7285dbf4f8")
	version("0.1.4", sha256="20335f4822a86ec9b3c04b48971f299e4052986360de6e17d3f8813b06ddeee5")
	version("0.1.5", sha256="412e7dafcbe087bdf0d731b4110d76b21759fb358b980fd67c113acf2f56ecea")
	version("0.1.6", sha256="42d08143545569f9ae2c677498064eb5cefef83fc511f550cca8fd459df9ccd5")

	depends_on("py-setuptools", type=("build"))
