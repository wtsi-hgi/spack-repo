# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBlake3(PythonPackage):
	"""Python bindings for the Rust blake3 crate"""
	
	homepage = "https://github.com/oconnor663/blake3-py"
	pypi = "blake3/blake3-0.4.1.tar.gz" 

	version("0.1.0", sha256="376f39ec7f2565adfdc20e46f9768ab729417786a2e2dc22180799bdf05f79f5", expand=False, url="https://files.pythonhosted.org/packages/53/ed/4faec95b9b40f9be267cf22ea43fe5caeb70f59b8ec6a05bdc8f385e06f0/blake3-0.1.0-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.1", sha256="3151a97d34544fe8a2831a015437b6887d010aa6a067f404269e3b85460232c3", expand=False, url="https://files.pythonhosted.org/packages/fd/12/e5a19b293b96b8806b60f6b0f3ebdedbfcfbdca6ea4c204dfd5df5b2a418/blake3-0.1.1-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.2", sha256="02252dd033ae79da164a4e96693f9bf95db62df70199b9274c9ab073b49c2ddb", expand=False, url="https://files.pythonhosted.org/packages/77/ad/8ef65bd3bd7461b32d09eb3499c6654e51251789d9bcfcc7534f20a16abc/blake3-0.1.2-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.3", sha256="8f053c2c3ab071ac87e985944c880ec9a16d4db38925d55f95f159c132ad3b50", expand=False, url="https://files.pythonhosted.org/packages/87/cf/8bd19e4e9653334cf1454c2d69e76a10a6b8b5c82dc8f066c267755a1aac/blake3-0.1.3-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.4", sha256="f2c24e889ddff8186f362fdf792e20006553db88708dec5b72706f3c8a7d5f27", expand=False, url="https://files.pythonhosted.org/packages/d7/d9/4740acd52573498efa4beddb98b3e4ecfe6f4a8c425e8c618fb2092cd802/blake3-0.1.4-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.5", sha256="beb254263af3f9139cbc149c7c141b2746110ba24e8ed9abf7ab1e0d9984711e", expand=False, url="https://files.pythonhosted.org/packages/71/a8/05f68bc7c1cd4ccb32707925a0fd3e578f42cc201e93bbaf84da30c51917/blake3-0.1.5-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.6", sha256="c2a44219a480251d7b2cc49af25cb69f377e988a897a070d5513a9c1d5aa0d80", expand=False, url="https://files.pythonhosted.org/packages/58/e4/88603a82928869103f330703efc7b118df11d3c91fc887c85b209c548a73/blake3-0.1.6-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.7", sha256="cc459bde85fce01b1b58b815d0c1df87b692cc8a434e70debe2f1a3737cf2a07", expand=False, url="https://files.pythonhosted.org/packages/e2/78/452ef34f6473932b4823bea1615fe2a24834868d59b2ab76fdb908a03c6c/blake3-0.1.7-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.8", sha256="b131129196ac4242bc9127a425daad46a8e7a451daef21a9337fcec17db445a8")
	version("0.2.0", sha256="9432148c58aa6f1d7ca08b87f5467c9708e6650b18af9733a6359ffa6cfac3de", expand=False, url="https://files.pythonhosted.org/packages/5b/3a/417cf4594dee08a039f662a619772a33b55440fd0bdc54bca09d3f9b484f/blake3-0.2.0-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("0.2.1", sha256="c4d1a317c1937e7ddaba4c8d5316f2c08b56ef7591662496f523a96848969022", expand=False, url="https://files.pythonhosted.org/packages/1f/1d/80bcfcdbb7a1f8d0a1311783eaa179383732937f9b61cbe42dc08f48a3c4/blake3-0.2.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("0.3.0", sha256="cf23225bddc5560ab7aa6a5142c6f7b8a6d63fae587893a984e26cfe8ee5f585", expand=False, url="https://files.pythonhosted.org/packages/49/ee/61899ec1e0ae507b68c2a4aa711160ea41f498a901bac3e3a0491aaf045f/blake3-0.3.0-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("0.3.1", sha256="1e3d2923bf9846fdda3bb037e4ecf25fd3b071784c3131ee14ce1468f0f26b0c", expand=False, url="https://files.pythonhosted.org/packages/88/49/711c212f7690b5a99caf4e73fb4bba9200c3ef0d3a05f488612152d0ab81/blake3-0.3.1-cp310-cp310-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("0.3.2", sha256="6d23147940d789cf0d482638344dc949f781b620e070bc1c00eb55a9e8d37cc7")
	version("0.3.3", sha256="0a78908b6299fd21dd46eb00fa4592b259ee419d586d545a3b86e1f2e4d0ee6d")
	version("0.3.4", sha256="4b7ef354144a2a19d7dbbfebce11735f68154e5190f9cc53825237bdb1bb78af")
	version("0.4.0", sha256="4238c834f94fb370b8f13c9f4de9576ee9a4824a6b9725d65cf6146fe72203d6")
	version("0.4.1", sha256="0625c8679203d5a1d30f859696a3fd75b2f50587984690adab839ef112f4c043")

	depends_on("py-maturin", type="build")
