# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PySccomposite(PythonPackage):
	"""COMPOSITE multiplet detection"""
	
	homepage = "https://github.com/CHPGenetics/COMPOSITE"
	pypi = "sccomposite/sccomposite-1.0.0-py3-none-any.whl" 

	version("0.0.1", sha256="dfcb4530a71c538a0c1478c40a1acfe9ff0707891e3d985a1d1fb1754162139b", expand=False, url="https://files.pythonhosted.org/packages/3e/e4/75d7b4bf01b45516c85405627c7f3c1c8057eb694ef72fd46b2811f731d7/sccomposite-0.0.1-py3-none-any.whl")
	version("0.1.0", sha256="403a94aac32eb0c5fc70ebba0f8debb198795ce13d80e5e3c0bfb523f7f0c0f2", expand=False, url="https://files.pythonhosted.org/packages/f0/f4/456133ff5a665125846a4758362c0490daf0b5c387e05c18b23ec5736c72/sccomposite-0.1.0-py3-none-any.whl")
	version("1.0.0", sha256="88dc504014e305e26d80cf081e7887bea1b4ef86d94fa9c29c9e1fdbc4a042ff", expand=False, url="https://files.pythonhosted.org/packages/55/0d/483666c65fd8c5c02d3093e27bcec955b0c69e1c9ec1c6629fbdf020b803/sccomposite-1.0.0-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scanpy", type=("build", "run"))
	depends_on("py-anndata", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-tqdm", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))
	depends_on("py-torch@2.2:+cuda", type=("build", "run"))
