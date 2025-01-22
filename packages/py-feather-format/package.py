# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyFeatherFormat(PythonPackage):
	"""Simple wrapper library to the Apache Arrow-based Feather File Format"""
	
	homepage = "http://github.com/wesm/feather"
	pypi = "feather-format/feather-format-0.4.1.tar.gz" 

	version("0.1.0", sha256="1175851705bc491ab2cf1b30d67aa2c01a664cc6320ed8e4adc50eabd85b13ba")
	version("0.1.1", sha256="de0465946cb4f87f2a101ae771f6cf2f53bfa6d94bfdeeb0f7050f3c5fd3e43d")
	version("0.1.2", sha256="2fb5610f1e8f7eaef4eec9f82ef6c7689b8ef55d593bc8eae70e2fd0611e86ce")
	version("0.2.0", sha256="28f83f3e02eb5b9ff32cea8a8b49905a65e6c1468b78f8a765efcb9fde047472")
	version("0.3.0", sha256="f959f3d886f78cb47c60171263a926c4b90aa3d7c514669fe0e3e1eae34bb67b")
	version("0.3.1", sha256="458c2a4293c6ec5428576947a6a526e0eda4dde212b154691b6d8d2e402c88f3")
	version("0.4.0", sha256="a7a0fbc727e1877354d4b4ad83f8e382a249f116241d0ccfc624cac24bddb1a9")
	version("0.4.1", sha256="45f67e3745d394d4f160ca6d636bbfd4f8b68d01199dc1649b6e487d3e878903")

	depends_on("py-setuptools", type=("build"))
