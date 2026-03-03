# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitMisc(PythonPackage):
	"""Miscellaneous tools for scientific computing."""
	
	homepage = "https://has2k1.github.io/scikit-misc/stable"
	pypi = "scikit-misc/scikit_misc-0.5.1.tar.gz" 

	version("0.1.0", sha256="ea59f872ab96c42dfe9a83d3ade6cec9a904ba1cfaffce46d3a2b8c580a55f6a", expand=False, url="https://files.pythonhosted.org/packages/06/c5/9a22176939ea2c4f2c85fa2b463d274d3d483592ed4cb23c06fd51b860e8/scikit_misc-0.1.0-cp35-cp35m-manylinux1_x86_64.whl")
	version("0.1.1", sha256="9dea0fde4c1b74bec9f8d54a27df7d3c139a62371a0bff022453ae2dc120fc48", expand=False, url="https://files.pythonhosted.org/packages/89/d1/87f120b39e4102ddcc345b8ed586a7253673009e3f283589ba45be095638/scikit_misc-0.1.1-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.2", sha256="995df1c651d75b34d1dea35eb66666b5b8cc043ae646db1756aa9c069c7d9b0a", expand=False, url="https://files.pythonhosted.org/packages/e5/43/af57d9c25b0e48c542264ee6ed344cbe4bffb5c349b93e14a4331dd72d97/scikit_misc-0.1.2-cp38-cp38-manylinux1_x86_64.whl")
	version("0.1.3", sha256="606f01509a00c3053739a5b60f861b8f84a96ccccea1a20a3e1f4932624acadd", expand=False, url="https://files.pythonhosted.org/packages/3b/70/1ccacc54bc3303010f92f17796eed61d801327ff65a7d7031993ba3c34e8/scikit_misc-0.1.3-cp39-cp39-manylinux1_x86_64.whl")
	version("0.1.4", sha256="5c01e261dc96312272efa8990524425009bc349d65f69e75fcaca08166567592", expand=False, url="https://files.pythonhosted.org/packages/15/32/287b8ebe32eb2265b561aad2bd59d7e63f35479bd3d1fa552ec48b2f384e/scikit_misc-0.1.4-cp39-cp39-manylinux_2_5_x86_64.manylinux1_x86_64.whl")
	version("0.2.0", sha256="ac14dd4e935e442fc34ab1c583b6611d4603d06f48828a85c7e03e2c2c582bbc")
	version("0.3.0", sha256="9a89b40a1f9bddb56212b87db9e5588867d5cf9490512a8209c1ac049efe36b8")
	version("0.3.1", sha256="ba813a005ab681df478d719d3c3f03eeda709b6a45e0c1a0056eaef0495c16e4")
	version("0.4.0", sha256="467825b58dbe0563a3a9259f28d4220db35819bf0ac25bb3e3c052d9c44fbd2a")
	version("0.5.1", sha256="c5c1f69ac5f84e0103f40525c7d28ecc0ee028314cbc9f07c497cc39143e52a3")

	depends_on("python@3.9:", type=("build", "run"))
	depends_on("python@3.10:", type=("build", "run"), when="@0.4.0:")
	depends_on("meson@1.3:", type=("build"))
	depends_on("py-cython@3.0.6:", type=("build"))
	depends_on("py-meson-python", type="build")
	depends_on("py-numpy", type=("build", "run"))
	depends_on("openblas", type=("build", "run"), when="@0.3.1")

	conflicts("meson@:1.2")

# {'numpy': ['0.1.0', '0.1.1', '0.1.2', '0.1.3', '0.1.4']}