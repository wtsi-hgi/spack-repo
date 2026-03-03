# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyBucketcache(PythonPackage):
	"""Versatile persisent file cache."""
	
	homepage = "https://github.com/RazerM/bucketcache"
	pypi = "bucketcache/BucketCache-0.9.1.tar.gz" 

	version("0.10.0", sha256="a61b81b4b876fe589d1b367d1eaa78ac9cdd2e3f1152dde6f616a4e5b48c7f9e")
	version("0.11.0", sha256="68dfd468e9100c8e0adf109c7eedfadbe287127dfcd272b232b268c82cc16dc9")
	version("0.11.1", sha256="cf139b34465dacdbaebd1c0acb1e52bcf94c476f0171868e2e9176492f99eea9")
	version("0.11.2", sha256="294e94cfd924a6dbafa9b37a73181e2aca93035b677b1869847ccb4eb049d559", expand=False, url="https://files.pythonhosted.org/packages/94/b2/1d2664db9c99937c32ac4e6c5b36b260e2da436452408c85079fd4bdc2c7/BucketCache-0.11.2-py2.py3-none-any.whl")
	version("0.11.3", sha256="9de578d4dd8f99b12fa78cccea6e22277a8e0c181b0f7fe217e8c45c79b3ac4a", expand=False, url="https://files.pythonhosted.org/packages/47/47/b33588cf3fb6137cf875d54e1beb25a5a886d9374104d98bbba3f4bfa556/BucketCache-0.11.3-py3-none-any.whl")
	version("0.12.0", sha256="07810f4905476a0353eda5aa4f28ca52405dbf852cdb9f2e5db50a4f2c267309", expand=False, url="https://files.pythonhosted.org/packages/2f/c4/c9086d409dc65f1abad2d12d35ed691a21ee4b0cf530154bea64e23334c1/BucketCache-0.12.0-py2.py3-none-any.whl")
	version("0.12.1", sha256="7f98a88431acb4b0f5ce9dc2cad81647bdeca2afb19c6814e47b856665bd77e6", expand=False, url="https://files.pythonhosted.org/packages/a8/32/3e29ed1ac289776e5e576132d7812c4ca702458db47527a78adad5d31d2d/BucketCache-0.12.1-py2.py3-none-any.whl")
	version("0.5", sha256="d25e64f618318ad044d59a894d2823987cdbd44ac84cd00e111931472b1b0f08")
	version("0.6.0", sha256="4bdce40c1ce197827f386ec846b88335e6709ca43891f49d3714adaa9aab768d")
	version("0.7.0", sha256="d9c92fc86dbaa615aa8619b6d037cca6590af07091acd4d59129f8fc74db4895")
	version("0.7.1", sha256="b456402f6377c84e1e348c30b6dfabe9a6b917028f6abe0f575875cc458588a8")
	version("0.8.0", sha256="48955360b890eca969652d0f00183088734a4be1c7c712c8af89d91e86fd4566")
	version("0.9.1", sha256="482cf26c9dbfa15e228886e33a758c8b1bc7ed70663ac46034dad9faf5df6f26")

	depends_on("py-setuptools", type=("build"))

# {'boltons\r': ['0.11.2'], 'decorator(>=4.0.2)\r': ['0.11.2'], 'logbook\r': ['0.11.2'], 'pathlib\r': ['0.11.2'], 'python-dateutil\r': ['0.11.2'], 'represent(>=1.3.0)\r': ['0.11.2'], 'six(>=1.9.0)\r': ['0.11.2'], "clint;extra=='dev'\r": ['0.11.2'], "mock;extra=='dev'\r": ['0.11.2'], "msgpack-python;extra=='dev'\r": ['0.11.2'], "packaging;extra=='dev'\r": ['0.11.2'], "pytest;extra=='dev'\r": ['0.11.2'], "pytest-benchmark;extra=='dev'\r": ['0.11.2'], "pytest-cov;extra=='dev'\r": ['0.11.2'], "pytest-xdist;extra=='dev'\r": ['0.11.2'], "shovel;extra=='dev'\r": ['0.11.2'], "sphinx;extra=='dev'\r": ['0.11.2'], "twine;extra=='dev'\r": ['0.11.2'], "mock;extra=='test'\r": ['0.11.2'], "msgpack-python;extra=='test'\r": ['0.11.2'], "pytest;extra=='test'\r": ['0.11.2'], "pytest-benchmark;extra=='test'\r": ['0.11.2'], "pytest-cov;extra=='test'\r": ['0.11.2'], "pytest-xdist;extra=='test'\r": ['0.11.2'], 'boltons': ['0.11.3', '0.12.0', '0.12.1'], 'decorator(>=4.0.2)': ['0.11.3', '0.12.0', '0.12.1'], 'six(>=1.9.0)': ['0.11.3', '0.12.0', '0.12.1'], 'logbook(>=0.12.5)': ['0.11.3', '0.12.0', '0.12.1'], 'python-dateutil': ['0.11.3', '0.12.0', '0.12.1'], 'represent(>=1.4.0)': ['0.11.3'], 'pathlib;python_version<"3.4"': ['0.11.3', '0.12.0', '0.12.1'], "pytest;extra=='dev'": ['0.11.3'], "packaging;extra=='dev'": ['0.11.3'], "twine;extra=='dev'": ['0.11.3'], "pytest-xdist;extra=='dev'": ['0.11.3'], "shovel;extra=='dev'": ['0.11.3'], "msgpack-python;extra=='dev'": ['0.11.3'], "clint;extra=='dev'": ['0.11.3'], "pytest-benchmark;extra=='dev'": ['0.11.3'], "sphinx;extra=='dev'": ['0.11.3'], "pytest-cov;extra=='dev'": ['0.11.3'], 'mock;python_version<"3.3"andextra==\'dev\'': ['0.11.3'], "msgpack-python;extra=='test'": ['0.11.3', '0.12.0', '0.12.1'], "pytest;extra=='test'": ['0.11.3', '0.12.0'], "pytest-benchmark;extra=='test'": ['0.11.3', '0.12.0', '0.12.1'], "pytest-cov;extra=='test'": ['0.11.3', '0.12.0', '0.12.1'], "pytest-xdist;extra=='test'": ['0.11.3', '0.12.0', '0.12.1'], 'mock;python_version<"3.3"andextra==\'test\'': ['0.11.3', '0.12.0', '0.12.1'], 'represent(>=1.5.1)': ['0.12.0', '0.12.1'], "pytest(>=3);extra=='test'": ['0.12.1']}