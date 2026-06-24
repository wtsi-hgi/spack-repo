# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyAssertpy(PythonPackage):
	"""Simple assertion library for unit testing in python with a fluent API"""
	
	homepage = "https://github.com/assertpy/assertpy"
	pypi = "assertpy/assertpy-1.1.tar.gz" 

	version("0.10", sha256="14f1405fb6fdb3ca24614ea714a6a9b64bae9e7d2a24c435c431a972522d4315")
	version("0.11", sha256="320260d25a8e25e2185bdbed71209e19a0981ba238444aa50817f293bfac8177")
	version("0.12", sha256="563502ad2d89f5242543924d1ae62472c24daeeaf2ecfd78b004feb0559395b9")
	version("0.13", sha256="3c288e81e1c5118b9722a1f396db21724916cfb480f3c0c079c4af91ee6f79ce")
	version("0.14", sha256="1b7e591f490616e3f2707b6e511b91b188a8c6facb3a4ff0db2339b0a41d73c4")
	version("0.15", sha256="04f52dcd9d60d074b3cfd9f16cc7b4dde4cdf654133562b754062947bc357775")
	version("0.5", sha256="f9710078c3fc23943596ba1427f822296d311c04d3887018bcd3e07039a32aa4")
	version("0.6", sha256="b85a26e6ac0e71a8294ed10de414a31bcab4753b7a83f537fd391e7616fc5d2d")
	version("0.7", sha256="306002c951b4344225e905492eaf4a1a0438a1107b3019f0f2ff5c41863e67ab")
	version("0.8", sha256="41b276d0ca179b5dd8aab3b5e7e9201e93a6d20103dbd36cd707d123a9f1ef0d")
	version("0.9", sha256="dd0d2e6d4de891fd992aca1a4c877162f50d23dd0d38fc7305fd01d9128e30bf")
	version("1.0", sha256="21b5923f1b49beaa96ed72fffe9991fcd869bd48583c80ec5d5a6e8e50f0df06")
	version("1.1", sha256="acc64329934ad71a3221de185517a43af33e373bb44dc05b5a9b174394ef4833")

	depends_on("py-setuptools", type="build")
	depends_on("py-pip@:22", type="build", when="^py-setuptools@:63")
	depends_on("py-pip@23:", type="build", when="^py-setuptools@64:")
