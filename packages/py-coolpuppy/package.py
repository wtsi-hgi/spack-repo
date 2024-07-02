# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCoolpuppy(PythonPackage):
	"""A versatile tool to perform pile-up analysis on Hi-C data in .cool format."""
	
	homepage = ""
	pypi = "coolpuppy/coolpuppy-1.1.0-py3-none-any.whl" 

	version("0.1", sha256="9305a85891e1bdaf84bd4fe2bea9a40af9e9ffdc332de3c928621e0df769dbff")
	version("0.2", sha256="e5d1f3c6e747fda52b6ae8514e72cd67157687b757c8ee17a0de72128c661e62")
	version("0.3", sha256="eca2bca77c8ad2cc169883ac17a28467fd0cc40927bafc37e423a965fdfb90d1")
	version("0.5", sha256="e2ff3dea55a735ff68a6e6405871f2d9d587319a98fec1c42e7819e4c44ea42c", expand=False, url="https://files.pythonhosted.org/packages/3f/cb/ca1bf3a4f869883d4c1a5d1a38e9c3fb80b2ae9e0f8c0bc9e4a05eb41651/coolpuppy-0.5-py3-none-any.whl")
	version("0.5.1", sha256="324f5182db241a8b5801786769c35bb562b06b5b935c1a0594bf4bb820ea32e0", expand=False, url="https://files.pythonhosted.org/packages/49/81/9ae12833ddac9ef030c7bf29e7957298c1b1a3829c82517c4519adbfc0c9/coolpuppy-0.5.1-py3-none-any.whl")
	version("0.5.3", sha256="be63736f621cc05e8b2a9b8a77186b3d6e994ea534f49aebaf0fbb2d6c243718", expand=False, url="https://files.pythonhosted.org/packages/62/c4/e33aed69556dfb77b6149b1a241e937ef222c97bf894e1c0b635e112cf88/coolpuppy-0.5.3-py3-none-any.whl")
	version("0.5.4", sha256="c272e59a03455952f1a4472610ee9698b7f12305b7a062e6e102fe3737d1aa84", expand=False, url="https://files.pythonhosted.org/packages/b8/41/b1d300b3e6982c6061ef57871ed766e54e84583af4efea0dcb9876b323e8/coolpuppy-0.5.4-py3-none-any.whl")
	version("0.5.5", sha256="d0761992959a37a3749ed51ad9daf88ff500db5a4d511ec485ff5fa35ea8cd3e", expand=False, url="https://files.pythonhosted.org/packages/65/af/14b866ae90d29b8def6896b3d4e943affca75b8b6ce73d6eea34175fc0e6/coolpuppy-0.5.5-py3-none-any.whl")
	version("0.7", sha256="6dc2b25f07fb2968a7293fe3b6d9bdfeaa9a41aa56d8ef033519640ff1511416")
	version("0.7.5", sha256="1d1af194849d10a48384af64c766c69d821caa404586da35d54e72e248fe9cc0")
	version("0.7.6", sha256="72558d396353b7693249af5fa05f266e988a41e9d64a7edd0a4a7e3958f655fe")
	version("0.8.1", sha256="85508c571996bb00ea362c175afe165b23c2f572eb6d276fc9e974b2c6cf968e", expand=False, url="https://files.pythonhosted.org/packages/55/c9/6a776a2bb8b44d8ade4f8290cd1fddeb83f3f353df6977f8a415a86bdd80/coolpuppy-0.8.1-py3-none-any.whl")
	version("0.8.2", sha256="58f088dde434a6065a75d1fc2301642ace568d1e880bfda941143821beac101a", expand=False, url="https://files.pythonhosted.org/packages/fa/9f/8601e9e8886cfc5727bcd9066e3391e19861e226f48474354ec8b5a46d93/coolpuppy-0.8.2-py3-none-any.whl")
	version("0.8.3", sha256="d1f731675b3b8146a6e4cf9e02f5b8f70c10ba4c46e8493b8a9ef6f3b5cc61eb")
	version("0.8.4", sha256="03d9cc3178826ee6494b092d2855ecd47e54798cdbb0a603a2d6b9d0b82367a3")
	version("0.8.5", sha256="3ac54cea016fb2079534ecbd7ff98515d8e228fadaa7d2936fa32d41ec2c2ac1", expand=False, url="https://files.pythonhosted.org/packages/e3/8a/98cbb67dea02d4fc6297d1c68d647e4823f74367c90b48565ba6e4d00459/coolpuppy-0.8.5-py3-none-any.whl")
	version("0.8.7", sha256="a27660bffa15400fac17c3f6fea860cf5c0f11dce6cbd1390a9a23a1b163cb17")
	version("0.9.1", sha256="29f518db58238f2b961a45bd3859d07a69c514c3427ad9b5028640955367ee66", expand=False, url="https://files.pythonhosted.org/packages/46/17/76486fe8120c3153244f3e16b751c481571c0c0380a1ba6f503358c9515b/coolpuppy-0.9.1-py3-none-any.whl")
	version("0.9.2", sha256="61c5eafd82c89ccc1bdb1d661068dfce37c8dd8a68c27f101086b64e691fd580", expand=False, url="https://files.pythonhosted.org/packages/ce/02/1d00688bbf721ea0623dfb9adab6fe1c5b26e5f3017481c3f70c213ef647/coolpuppy-0.9.2-py3-none-any.whl")
	version("0.9.4", sha256="05946efeaf69d6527ef402cbfa6d30fe66ce4250685c27198e44768d448b018b", expand=False, url="https://files.pythonhosted.org/packages/a3/8f/b55bd91325beb35226c3e861c95618079dc511709bef23af2370dc56a9ee/coolpuppy-0.9.4-py3-none-any.whl")
	version("0.9.5", sha256="b9233f9920fce12d3da95893441ab3f933b194d72ff897c02cea3753ca8b4d40", expand=False, url="https://files.pythonhosted.org/packages/1d/5b/670a1bd583e6af33c7e1b92512db35b9e8fa0b10f6c0756f0e41d9f570a5/coolpuppy-0.9.5-py3-none-any.whl")
	version("1.0.0", sha256="ad514b909cb6cc8a25c808a21b0d83865ecd62ff4f0ca51aff060a3afcc939f0", expand=False, url="https://files.pythonhosted.org/packages/25/a9/e49820faaa5a3b93926fb585e7be338f68b59d208e2bc5414c21aa3cf523/coolpuppy-1.0.0-py3-none-any.whl")
	version("1.1.0", sha256="70d5af3451da6fe122f2349658d06e6ff5378e353208dc84bbfb37387e1bffd7", expand=False, url="https://files.pythonhosted.org/packages/43/66/9fc3c0e81ed41e8c6daba9fb4227cb9fee160a913d841f6a66915cf7f3b2/coolpuppy-1.1.0-py3-none-any.whl")

	depends_on("python@3.8:", type=("build", "run"))
	depends_on("py-multiprocessing-logging", type=("build", "run"))
	depends_on("py-h5sparse", type=("build", "run"))
	depends_on("py-m2r2", type=("build", "run"))
	depends_on("py-natsort", type=("build", "run"))
	depends_on("py-seaborn", type=("build", "run"))
	depends_on("py-matplotlib", type=("build", "run"))
	depends_on("py-bioframe", type=("build", "run"))
	depends_on("py-more-itertools", type=("build", "run"))
	depends_on("py-pyyaml", type=("build", "run"))
	depends_on("py-cooltools", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-cooler", type=("build", "run"))
	depends_on("py-cython", type=("build", "run"))
	depends_on("py-h5py", type=("build", "run"))

# {'cooler': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'cooltools': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5'], 'natsort': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'numpy': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5'], 'pandas': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'scipy': ['0.8.1', '0.8.2', '0.8.5', '0.9.1', '0.9.2', '0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'Cython': ['0.9.1', '0.9.2', '0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'pyyaml': ['0.9.4', '0.9.5', '1.0.0', '1.1.0'], 'h5py(>=3.0)': ['1.0.0', '1.1.0'], 'numpy(>=1.16.5)': ['1.0.0', '1.1.0'], 'cooltools(>=0.5.2)': ['1.0.0', '1.1.0'], 'more-itertools': ['1.0.0', '1.1.0'], 'bioframe(>=0.3.3)': ['1.0.0', '1.1.0'], 'matplotlib': ['1.0.0', '1.1.0'], 'seaborn': ['1.0.0', '1.1.0'], 'm2r2': ['1.0.0', '1.1.0'], 'h5sparse': ['1.0.0', '1.1.0'], 'multiprocessing-logging': ['1.0.0', '1.1.0']}