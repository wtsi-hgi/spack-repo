# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDeepswarm(PythonPackage):
	"""Neural Architecture Search Powered by Swarm Intelligence"""
	
	homepage = "https://github.com/Pattio/DeepSwarm"
	pypi = "deepswarm/deepswarm-0.0.9-py3-none-any.whl" 

	version("0.0.10", sha256="ec5e0f2e68219f110dbe8bf5d7188dcb8291032f2c5d2135bfccdc867bd8a57e", expand=False, url="https://files.pythonhosted.org/packages/e4/67/cb9a136d1d1b63dab32c42bad37fd99d9dc3fac858958cdc81fc644df8ec/deepswarm-0.0.10-py3-none-any.whl")
	version("0.0.5", sha256="b37a7c1b979b72484493e89e0069676e98c62640579a56b5711331e7d1dd5c1e", expand=False, url="https://files.pythonhosted.org/packages/ae/10/be17e69953cf4b8230db20cb84b44a5a12a1573acd4e4688fd0184f000cb/deepswarm-0.0.5-py3-none-any.whl")
	version("0.0.6", sha256="30282e7e062669e3d7f27cac8911f01047d042430238d25cd9e1a2c0387e14c5", expand=False, url="https://files.pythonhosted.org/packages/3f/da/94e0a119f51cf36e1af17383190e3ef7d0397c99e11b453cda5205015115/deepswarm-0.0.6-py3-none-any.whl")
	version("0.0.7", sha256="e7ea850268f0209ad1356b4ba9a36a9b9faafe71d5eef8c51b2a38c39881668b", expand=False, url="https://files.pythonhosted.org/packages/d3/84/81a3076b3f603dd2f7e3521662e61cb51eb02c30b454f6be02b591ef96f0/deepswarm-0.0.7-py3-none-any.whl")
	version("0.0.8", sha256="ee1d2cfe6cd84f3837a5f3dbeb8e6266027bd5b69c851a7e6dff0455373723cb", expand=False, url="https://files.pythonhosted.org/packages/e4/97/9e2247e2135f3e7f95cbd14294d12a0425156584e936ffc127bcfab88182/deepswarm-0.0.8-py3-none-any.whl")
	version("0.0.9", sha256="ba882ca720ce365542d1514d7f9403c1a81a71348ad86200e6a02fba2025aca0", expand=False, url="https://files.pythonhosted.org/packages/62/6c/5db6a768748005370c6eb46da0e07311f9df863f7716159e317be1ab02d3/deepswarm-0.0.9-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-colorama", type=("build", "run"))

# {'colorama(==0.4.1)': ['0.0.10', '0.0.5', '0.0.6', '0.0.7', '0.0.8', '0.0.9'], 'pyyaml(==5.1)': ['0.0.10', '0.0.6', '0.0.7', '0.0.8', '0.0.9'], 'scikit-learn(==0.20.3)': ['0.0.10', '0.0.5', '0.0.6', '0.0.7', '0.0.8', '0.0.9'], 'pyyaml(==3.13)': ['0.0.5']}