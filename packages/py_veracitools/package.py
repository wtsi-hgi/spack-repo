# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyVeracitools(PythonPackage):
	"""Testing utilities"""
	
	homepage = "https://github.com/pepkit/veracitools/"
	pypi = "veracitools/veracitools-0.1.4.tar.gz" 

	version("0.1", sha256="3fd8e51640fcc2c7c4067508f32d42f0fb1ec08e72924fa68743ea599b22ce0d")
	version("0.1.1", sha256="fc9aa318ffc915cf2e6cc0f75aa01dcf5a0e3e46e37364cc99788ae7330f9084")
	version("0.1.2", sha256="3bcca83c514ee5af1844093985b7d180e7f3924b1046b7c27127122a3967bb94")
	version("0.1.3", sha256="422764b1e8eec3023212f6640b40c120b5d93dad5f17fa8d2fca34d994536df7")
	version("0.1.4", sha256="5c86d36a8567b3da1b0ac296b4668cb9a9ea8e18f3c8c18eb88373aca8312a37")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-pytest", type=("build","run"))
