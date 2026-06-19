# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyMappy(PythonPackage):
	"""Minimap2 python binding"""
	
	homepage = "https://github.com/lh3/minimap2"
	pypi = "mappy/mappy-2.9.tar.gz" 

	version("2.10", sha256="012a5f4df1ffa7bef98b22baaf904e0b4ea209ae0621805e630397b9e9f03032")
	version("2.11", sha256="3a76eb65a9a8add70d59e4e733c7cfdbf3ec7995435a6913143f54bdf6433461")
	version("2.12", sha256="54645383ef0ca447b14a28d4621f87052c4b383443a4445f2ccd443c53279573")
	version("2.13", sha256="6a5008d53a44b157f39c5578fa6dce33ef3989270156f5e0a8fa08a19cfed21e")
	version("2.14", sha256="3015c03141d3c7378329910f920d43739e569302245d602c60c31a9c5e864525")
	version("2.15", sha256="78881c69e3b5c8422a3379819902204e78f6ae51b1e1b96754d6fc41efa41a3d")
	version("2.16", sha256="5c30f2196c0da8fc88a88147be2e035d3f5123fd6798a4ea4f8d854e5b040e4f")
	version("2.17", sha256="ed1460efc9c6785df28065b7e93e93c92227f623a181f1a852dca6e6acb1a15f")
	version("2.18", sha256="18fffdb4b831cc3f5399b919b0942c640bf9a943ca22102ac446f53af3b905a8")
	version("2.19", sha256="cd46ea643d18d8901e379914b4a1266c16c799263695ba969cce0bd85e2fb3f9")
	version("2.2", sha256="3e997012313e32317719b60ee3092e64d8e29d132f21ac9821f187523e409f1d")
	version("2.20", sha256="00c8720783ac982b514b01b86349ede9809eeaccdf1328acb5a16dfeef51458b")
	version("2.21", sha256="005c6c1981f39e695b2cb4316942fa9a37e677e7604197b21fc5c71cc1093f72")
	version("2.22", sha256="219c93ab7f8d5d7c26face512a9e738a7306f3376ebfa3017eac70676ba97840")
	version("2.23", sha256="8c756bafe21c60276cfd9bbff836bf0f0c4e1575742d65ed51bf4fa1437424a3")
	version("2.24", sha256="35a2fb73ef14173283d5abb31e7a318429e0330c3be95851df38dd83d4ff9af9")
	version("2.25", sha256="fd89fc1c8691aaa783cc453158a59f7ab6e185b431cbdf11d552fbcf1bbbc481")
	version("2.26", sha256="e53fbe9a3ea8762a64b8103f4f779c9fb16d418eaa0a731f45cebc83867a9b71")
	version("2.27", sha256="47df11e7cecee9138680d6d2312e44397d0484a02ecf1f5908dea50d94a0efe4")
	version("2.28", sha256="0ebf7a5d62bd668f5456028215e26176e180ca68161ac18d4f7b48045484cebb")
	version("2.29", sha256="43dda2693c963152ddb5be9eac2b7ea0c943cba9becd79494a9f2b8804039a9a")
	version("2.2rc0", sha256="a18537193a3ec01658d114c61bfd2e5b023c336c7f7a468b536e51b8f0f49766")
	version("2.2rc1", sha256="8391d6a2b74a158d47af97718cc06b1555a79e0d324a1a1c3526fa2ab791633b")
	version("2.3", sha256="238bb937744dae505d7375bbd0bebb9b25d0e7c6476d1db465471b0074fa5339")
	version("2.30", sha256="a25448004558a28cb0d74fb1e55b6ffe9a78aa15dd6b2763630fbbabbaa97a27")
	version("2.31", sha256="152a358c11cba1f992968e2611f1e0a1f4a87aaaa3602d93e4f59d7c1db8f3b2")
	version("2.4", sha256="25e2681c20a72c0425358380a8890eed9d4c21177e64d6bc973f597b3f03e87f")
	version("2.5", sha256="a2615232af1ac9d59192bc04efabc8962158a3aebe18dd83e4c15ffc377e4442")
	version("2.6", sha256="c4c49eec4b1b6e0c676e1e68a534d893f413fc04f473f38d286c1c357650f508")
	version("2.7", sha256="c690b8a5aff8dc450d4cb7d5b2013330e0fa6340612fa5f7aaa74f0f5085e4a8")
	version("2.8", sha256="7e7b26ed6c93fb6e3b9bd01df36c8ee55a4516d410057cd6ebef3a6d684f4542")
	version("2.9", sha256="49b2b784e4003358e1ef16d42900be73743cffd61bb91705b3fa6aebae1ccdfd")

	depends_on("py-setuptools", type="build")
	depends_on("py-pip@:22", type="build", when="^py-setuptools@:63")
	depends_on("py-pip@23:", type="build", when="^py-setuptools@64:")
	depends_on("py-cython", type="build")
	depends_on("minimap2", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
