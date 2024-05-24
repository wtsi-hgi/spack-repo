# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPtitprince(PythonPackage):
	"""A Python implementation of Rainclouds, originally on R, ggplot2. Written on top of seaborn."""
	
	homepage = "https://github.com/pog87/PtitPrince"
	pypi = "ptitprince/ptitprince-0.2.7.tar.gz" 

	version("0.1.3", sha256="f9badbb0cb39bd8d7ceb811d34ab2278e7883a653f0237c0590438bb62cccf6a")
	version("0.1.4", sha256="01955daa420a2bc66655af015b2d0134fb4b8cf058edc1e48f2e64981be5aa43")
	version("0.1.5", sha256="3e086063d8e4376ec8f5bd24e4d9475311b50eda968288817f1291e0aa5120b2")
	version("0.2.3", sha256="22955b66d2295b76e8e8bc3e2c4e50e3f6d54278f2fe80357a1fec903c528b1a")
	version("0.2.4", sha256="35d856c600f723f5b1315a47c155aa74ac4a7722e8d35d6233845083a3d5cad6")
	version("0.2.5", sha256="1b3dbac736f1180d865b9ae2508f2ce59769fc85800cbee120d2a3cbc67c6368")
	version("0.2.6", sha256="800b3688231a0b5244ed2696228c0f16dff86bf053aede44e424e9dbde484436", expand=False, url="https://files.pythonhosted.org/packages/dc/95/c3b9e3883f4ac06566a042db282167f5da14491fccaac538f8805612a62e/ptitprince-0.2.6-py3-none-any.whl")
	version("0.2.7", sha256="bbd19d4f8615935ac1b750651907303913fbdddc3fe864c1cb80faa3a2a3acfb")

	depends_on("py-setuptools", type="build")
