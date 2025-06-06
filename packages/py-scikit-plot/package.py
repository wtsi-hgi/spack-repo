# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyScikitPlot(PythonPackage):
	"""An intuitive library to add plotting functionality to scikit-learn objects."""
	
	homepage = "https://github.com/reiinakano/scikit-plot"
	pypi = "scikit-plot/scikit_plot-0.3.7-py3-none-any.whl" 

	version("0.1", sha256="f3785d6a2058138074fbcdb9b8987b62ef101a3b77001877546bc4b936114439")
	version("0.1.dev0", sha256="21263b33ab1a3e75ead43de5ff009f82b1504a16404b1385fc3e9b64abbc2ac5")
	version("0.1.dev1", sha256="007fbbc735cc5c79d377708f63580e74d348a0c6333774caa80149b7abe5e2c0")
	version("0.1.dev2", sha256="98cf24e4c038be2930fcd51acd8fd99c1becf2e519acd295f31c0294fd0531f7")
	version("0.1.dev3", sha256="49172228dae0fdd69e9c27e143676e2324437ac741d342d5802c7f031f04cc66")
	version("0.1.dev4", sha256="ea18ab1dffc75606adf374aad9baf8e785636a6aef1eaec9291f49e73e219edb")
	version("0.1.dev5", sha256="45e6775423884eb27ca166c85c4fddc1434f5d6a66508a96bbd0abad499c9f70")
	version("0.1.dev6", sha256="1d55e8089351cc6eaa05f1ce32e18f0cfc597a92dc9c0a66a7e73caf92bd0981")
	version("0.1.dev7", sha256="ae3a1cc88deccbee63e6e50329656146f1ec95782583371f7839be0b1f00234a")
	version("0.1.dev8", sha256="acb7eba29fdb1ac5205e05ef745ab9cf195a8831cc11f0f3e942bff274663521")
	version("0.2.0", sha256="fee4bbb7b6aced2b10045fe8d35c71f4d6d61b89bf2d112f89bd5a6ed560203e")
	version("0.2.1", sha256="ec49c24c884dcd68a538a60c114025ce31500d6dda770d0d5a4ed4f3410485b1")
	version("0.2.2", sha256="fd4ee3da9e8b587480733efbbfe8e0a5a498fe7451e09d5935bb93d8ff3c9736")
	version("0.2.3", sha256="404f17f633116fe899bcb4d5f7f909959afa00698f37727852a3a9102ba1a3b6")
	version("0.2.4", sha256="f4e8282c8f7c09a4400b732a7a6a5411a4b15114f5eab027d15e1b0179bf24d0")
	version("0.2.5", sha256="91b935c3996a32a435d1797d05178a1868ccb0537bfd4dc868b716d895cc227c")
	version("0.2.6", sha256="01b4f945f4e9ff48c04d861755a0417bd04c0ab8ac8b6fd5e5af804bd63762c9")
	version("0.2.7", sha256="570b0e055fd3c57be19372027fe89eb67ea4fe0294df81d485b4b3de2c663b48")
	version("0.2.8", sha256="3d8572420466d8ba980613570276a72467dea746f8b8996027a170f6b0029839")
	version("0.3.0", sha256="7ac4413b282ce82fb7ce257fee0bbcceda3a053fc6141e7d210bf43361be5fca")
	version("0.3.1", sha256="11d3ac10adbd3ada98e7b67a2f6dad0174b1e944dbe6af810a53bb5cc5d3271a")
	version("0.3.2", sha256="e4c0c5b290a1ecf302df8f16f9b09d10ab1737aff12377745e4fa04817ce93e5")
	version("0.3.3", sha256="b18e121535a0d2cfdde268c8c0437774da572e38474b84eed3b09d710572fae6")
	version("0.3.4", sha256="e2bdd974bd98cbf7dce5a505cd4cff9d819dd80580457c3bd4ce14889c250ef6")
	version("0.3.5", sha256="60faf903d3c3ffe4f849611450fb5f06f0c175d350c6f8746c5460fd1419ad28", expand=False, url="https://files.pythonhosted.org/packages/68/c7/81329c5ec9efb654cd57fbad0a044d8d84606b72ced564f96ff281238dc1/scikit_plot-0.3.5-py2.py3-none-any.whl")
	version("0.3.6", sha256="5ad12964c7d559dc0bd572b551f122dfc51b27c44986ca4b9101b694ff127756", expand=False, url="https://files.pythonhosted.org/packages/2a/4e/7cf08780801e30a08da283c3fb27c07eebeeebb9730b2c091ab1e37c43aa/scikit_plot-0.3.6-py3-none-any.whl")
	version("0.3.7", sha256="6b3d529800b32a899c54dc5761a93c63cbff482b1889a4afee57dd219f3ef0c3", expand=False, url="https://files.pythonhosted.org/packages/7c/47/32520e259340c140a4ad27c1b97050dd3254fdc517b1d59974d47037510e/scikit_plot-0.3.7-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-joblib", type=("build", "run"))

# {'matplotlib(>=1.4.0)': ['0.3.5', '0.3.6', '0.3.7'], 'scikit-learn(>=0.18)': ['0.3.5', '0.3.6', '0.3.7'], 'scipy(>=0.9)': ['0.3.5', '0.3.6', '0.3.7'], 'joblib(>=0.10)': ['0.3.5', '0.3.6', '0.3.7'], "pytest;extra=='testing'": ['0.3.5', '0.3.6', '0.3.7']}