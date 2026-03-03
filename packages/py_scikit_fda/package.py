# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitFda(PythonPackage):
	"""Functional Data Analysis Python package."""
	
	homepage = "https://github.com/GAA-UAM/scikit-fda"
	pypi = "scikit-fda/scikit_fda-0.9.1-py3-none-any.whl" 

	version("0.10.1", sha256="9db5817a7a70f0c1d7c2449dedd1196b25e787d8cc5a6c891cf772a395aec8ee", expand=False, url="https://files.pythonhosted.org/packages/98/8f/cb691eb94fd2361cafa7d9ee4a83d9482feeff970c4c6e6cc033fca17f6c/scikit_fda-0.10.1-py3-none-any.whl")
	version("0.2", sha256="1a4c8ab7826fae9f78cd8edfbe5df20867208123f2af62d534d192d3c483233b")
	version("0.2.1", sha256="a8d815cec5b6f15af9db7bde858afbf9d9df6517bdf214ecde2c54c174a5846f")
	version("0.2.2", sha256="78d967857718230998a296ab9990c8b4a4d630bebd5213879e8bc831a87fea5f")
	version("0.2.3", sha256="f42af721a1e49cc6754b7e946596ac1cd783126364f707d31b6ead1458a0a8fb")
	version("0.3", sha256="4e557b7a522b51f4b93cb607c2e960fafbe4c61b66769b32bea8b4d3290be8ba")
	version("0.4", sha256="61ecf491ed5b20fe9b3ec9d4966bb13b79971af8ae0f893b477ddd878e631fd4")
	version("0.5", sha256="5f383a27b4433f89ac1ad43ca8c45f1e21f83078a20e719efb75f5415a67643f", expand=False, url="https://files.pythonhosted.org/packages/c0/5a/e812a8e32318119079bce3374ff98ae304bce627448f0edfae753e6712f8/scikit_fda-0.5-py2.py3-none-any.whl")
	version("0.6", sha256="ea84a811b9020f0f0bd76c9366d59dc4ed2ab82d2cb556b1364324480cd62b96", expand=False, url="https://files.pythonhosted.org/packages/f6/2a/289ff2ae39e79f7ba6b610eb60498a5f1b18f7f4ce2bb9dfe23abd272ec6/scikit_fda-0.6-py2.py3-none-any.whl")
	version("0.6.1", sha256="c87c41bb3f00092b9baf2517458d8b5727d4ee1b035dd9e119a759f397e0ee98", expand=False, url="https://files.pythonhosted.org/packages/d4/98/de6570d91bf866f994b4c48b03db9b4275e98a6ab2ec34d2cc04f7376587/scikit_fda-0.6.1-py2.py3-none-any.whl")
	version("0.7", sha256="9352ec984deb3668df5e32963ec3a9aeffed82a8d79a6d709b176e4f57172a95", expand=False, url="https://files.pythonhosted.org/packages/5c/d2/28a9d399df7c06be8eed6776f8a6c411bbf8691d07c6bb9f488a9ee5fd7f/scikit_fda-0.7-py2.py3-none-any.whl")
	version("0.7.1", sha256="7228431350f5f913435981ecc228fd80f5f1abcc51e1d3961991907ac66c55bd", expand=False, url="https://files.pythonhosted.org/packages/06/71/c03a9a5db2ff4e669f966fbf50f8e33fde11286da288977646e55b205239/scikit_fda-0.7.1-py2.py3-none-any.whl")
	version("0.8", sha256="b4d3addd539b0bbb37b7ecc9c3992623d3d3221fc8a6cfdf1df0082bb8b12d09", expand=False, url="https://files.pythonhosted.org/packages/c4/70/08bab053f2f2e981a870400e181bf60d239268cbc9fc5bbadd00a2a4fd51/scikit_fda-0.8-py3-none-any.whl")
	version("0.8.1", sha256="ee58381c9a51278633e5bfab049840131d38ceaefe0d4e18c896779e0ef16c1b", expand=False, url="https://files.pythonhosted.org/packages/ad/44/61bef5be772047c7aac89d1c47bc29b8dec02ca13eb0cad5b5b6fb9a210a/scikit_fda-0.8.1-py3-none-any.whl")
	version("0.9", sha256="082d19c7ae502a7630d2860788c8172456733725d046d4c59ea281f25557e893", expand=False, url="https://files.pythonhosted.org/packages/f9/57/40d6311b9d846831ebf6b125fd558fce0a6ea51d59258508bbf71b517b30/scikit_fda-0.9-py3-none-any.whl")
	version("0.9.1", sha256="615bfb173d25ca495793a226248f65c193efc49fa942cf8bf94c0387099e5d63", expand=False, url="https://files.pythonhosted.org/packages/26/e2/f748588fbedc883749e2ce30312c6a1fa7f4abead686c4d7ca05169c5c9c/scikit_fda-0.9.1-py3-none-any.whl")

	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-dcor", type=("build", "run"))
	depends_on("py-fdasrsf", type=("build", "run"))
	depends_on("py-findiff", type=("build", "run"))
	depends_on("py-lazy-loader", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-multimethod", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-rdata", type=("build", "run"))
	depends_on("py-scikit-datasets", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-typing-extensions", type=("build", "run"))

	@run_after("install")
	def install_test(self):
		self.spec["python"].command("-c", "import skfda")
