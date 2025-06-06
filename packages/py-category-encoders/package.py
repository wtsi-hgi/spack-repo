# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyCategoryEncoders(PythonPackage):
	"""A package for encoding categorical variables for machine learning"""
	
	homepage = "http://contrib.scikit-learn.org/category_encoders/"
	pypi = "category-encoders/category_encoders-2.8.1-py3-none-any.whl" 

	version("1.0.0", sha256="5af4befe1a6cd80033afa926d1d9e53f33cff742770d09ccbd2ea0189031d28a")
	version("1.0.1", sha256="6bd4bb8a6281ff68ef2124946d25522c1c0f17003e5c877a82b939ca759faf7f")
	version("1.0.2", sha256="96154d29e7b3cdfbf5c9249acdb306959e494aa4f4fc75957502d2b068be4bd9")
	version("1.0.3", sha256="8cc8325b092a1440b3e6ab4033ee7599a8b9522e5ee1fcb492be327fc32dda4c")
	version("1.0.4", sha256="de3a13422562eef3151497e11306db7c376521e8d65a366fe046fff85c2ab05d")
	version("1.0.5", sha256="c619de6e0348703f79f8c490f9dfeb89baf44be0ecc32ba9207d8f06c641a2ac")
	version("1.1.0", sha256="57a26d01ca1db061b2f59fd7bbc4b3bb3cc3761ad785573f27714f9ad96c69c5")
	version("1.1.1", sha256="12df677a714a49f8b364b2bb52a1106969f1733ffb647175a19e653868c22994")
	version("1.1.2", sha256="bd502aaf440ebc7166ecc89ef666c4b128f99b87dca7396f8c6c4f57502c7154")
	version("1.2.0", sha256="0945a6b671ed443c63e7b7ad10c298e8affd3abd624b713d19bfb404a0fd1670")
	version("1.2.1", sha256="cabaca00e845fbddfaebfbedb670a078f53f943abfdf18173663100e5bd44ec1")
	version("1.2.2", sha256="858de8025caf1a6474cf879900ec9659cc0782ab6a93210823626341f6c4e075")
	version("1.2.3", sha256="e20bf223772725bee4586b703f41bfd18238c0a1ff38dd0cc8d1c8ec786d52cf")
	version("1.2.4", sha256="b3342686fcb9718e6475b48a725477da06cf9bce0345e9484b4cad9cd1ff5e2e")
	version("1.2.5", sha256="ba011dd4dfc817466aaaa6dc2ff9dea5f378536396a726e0ed74c207f315beab")
	version("1.2.6", sha256="99ccf0e451035d26dcfe9b21bea6835307b1ec090c289c5462001d3ad15f5bd0")
	version("1.2.7", sha256="8a2d44b4eae4072b61daf5a186b49aa84a7ea6e8966f78174faf12ea32d43f7a", expand=False, url="https://files.pythonhosted.org/packages/ea/19/2a897120eb9f9edcfe6b782e69626fcc7febf224c253577e953ee7dbc4b2/category_encoders-1.2.7-py2.py3-none-any.whl")
	version("1.2.8", sha256="ede61a429d14152be34e5d20ccf9c82899101b1d1d97e1544d29364537055caf", expand=False, url="https://files.pythonhosted.org/packages/a4/dd/660f7d3c8f344df3537dae1c4a96b92962ac4f470cf6fb763722cc420437/category_encoders-1.2.8-py2.py3-none-any.whl")
	version("1.3.0", sha256="f8c48db0214ab0fb5edb44e1c1df57bad1d358c2fb684e3d4689e678e5b9e723", expand=False, url="https://files.pythonhosted.org/packages/f7/d3/82a4b85a87ece114f6d0139d643580c726efa45fa4db3b81aed38c0156c5/category_encoders-1.3.0-py2.py3-none-any.whl")
	version("2.0.0", sha256="cbf6d8b47d63aac03d60d62c519e944709f2439ac57c1794dd606b25ba2dd40a", expand=False, url="https://files.pythonhosted.org/packages/6e/a1/f7a22f144f33be78afeb06bfa78478e8284a64263a3c09b1ef54e673841e/category_encoders-2.0.0-py2.py3-none-any.whl")
	version("2.1.0", sha256="a3f214fdfbd26e86e7809d44b3fea9d292a617b4b50b39f329116bae5b07f62c", expand=False, url="https://files.pythonhosted.org/packages/a0/52/c54191ad3782de633ea3d6ee3bb2837bda0cf3bc97644bb6375cf14150a0/category_encoders-2.1.0-py2.py3-none-any.whl")
	version("2.2.2", sha256="3704d140d873c1325e68051ab2dce9663fd57c77fb1c368b9dc02e82e80c176a", expand=False, url="https://files.pythonhosted.org/packages/44/57/fcef41c248701ee62e8325026b90c432adea35555cbc870aff9cfba23727/category_encoders-2.2.2-py2.py3-none-any.whl")
	version("2.3.0", sha256="3add1cc86d1a36256c0c8a45f89574244f4a19da42cc98fd831499ecfc46f80b", expand=False, url="https://files.pythonhosted.org/packages/6c/7e/6b9868e5540252cc8a28418e4d96bc390c5dc8745ad872d899dce44f765b/category_encoders-2.3.0-py2.py3-none-any.whl")
	version("2.4.0", sha256="c0e0517123e9a98c738b9924e35ffcdede06d74fd3002d5c9e335b97cb48954a", expand=False, url="https://files.pythonhosted.org/packages/c6/8d/3e311afef42e48d226a78b376799507543a5339af8187d79f04d07015ba8/category_encoders-2.4.0-py2.py3-none-any.whl")
	version("2.4.1", sha256="401d2b49d04467de179dae79b07bbd47c47c97018a9d5fbd1c1f2b5c5148f231", expand=False, url="https://files.pythonhosted.org/packages/78/f2/c63d4d8812e32e45fdc193c7a215fd1a59936f3be6175a02f9fff56e65ee/category_encoders-2.4.1-py2.py3-none-any.whl")
	version("2.5.0", sha256="f8dd75821956de85818c57ef6c43bd0419828404a0c2145051016b36da3d7e95", expand=False, url="https://files.pythonhosted.org/packages/27/d9/2fd411c0585ae69308bbc7e81f98ec8345c968718e865f3507671bf366df/category_encoders-2.5.0-py2.py3-none-any.whl")
	version("2.5.1", sha256="6055e10bef96897b2d8f56a9ef5065f9c9db0ad9c15496bbaa93f4b1e928087f", expand=False, url="https://files.pythonhosted.org/packages/b5/b0/4dd0f36b2e467676deebb605067251dd77a3d3864edfd65ade13c115e5b6/category_encoders-2.5.1-py2.py3-none-any.whl")
	version("2.5.1.post0", sha256="edf5b5c9d90827b86e0613f6f1b0ea109075e9c4978fa51642e833b19452d0ae", expand=False, url="https://files.pythonhosted.org/packages/4a/0d/e825642ae6f15a70bee5d0481ce3861f00dee0e93f1b6eca98a03a109d1d/category_encoders-2.5.1.post0-py2.py3-none-any.whl")
	version("2.6.0", sha256="d20d0149b823a53dc85e14b7cac5f01d3bc7c5ac2e42f3761f575cb504a35e7e", expand=False, url="https://files.pythonhosted.org/packages/8b/9f/09d149aab1296254fe83e34aaddc59ade820acb15d529773d753df3384bf/category_encoders-2.6.0-py2.py3-none-any.whl")
	version("2.6.1", sha256="d2b1d366ba1164ea1bc3bb1ddfa42c635a17c8991d1a4ba5e63d944ea2121845", expand=False, url="https://files.pythonhosted.org/packages/96/82/0cf7cb3922f9eb408e400b134b82437fc2898286b26e8cdf7cd5218ec71b/category_encoders-2.6.1-py2.py3-none-any.whl")
	version("2.6.2", sha256="5bec75df50f59da7c65b4beae27237d377150c9f0457a797430b5f5c27098855", expand=False, url="https://files.pythonhosted.org/packages/1f/e2/495811f12b2e90753fff0e42a07adb0370a725de17cc23a579ac9d3ca67c/category_encoders-2.6.2-py2.py3-none-any.whl")
	version("2.6.3", sha256="117775f1775e53a67c9e91842ac9100bc364cddc9f4058188796532bc5b11f1c", expand=False, url="https://files.pythonhosted.org/packages/7f/e5/79a62e5c9c9ddbfa9ff5222240d408c1eeea4e38741a0dc8343edc7ef1ec/category_encoders-2.6.3-py2.py3-none-any.whl")
	version("2.6.4", sha256="59f4b541ec787dfdfacc12267e1aff91a1ddc0b756991ec2129d50d6495d6e36", expand=False, url="https://files.pythonhosted.org/packages/98/47/598b4bf0ccf6f02915e71bdd23fe846a27adc2d3ba734f2ba5215d8e44f5/category_encoders-2.6.4-py2.py3-none-any.whl")
	version("2.7.0", sha256="62c50d06c296cda69335ac3997456368a4d6eeabea0c15100db52235227c0758", expand=False, url="https://files.pythonhosted.org/packages/cb/db/994342594822cd7ed9bc9bb67d259f2585e9034d07df9bae12133319914a/category_encoders-2.7.0-py3-none-any.whl")
	version("2.8.0", sha256="9958e89acff5614625b03f2d2e66a192b2daf03d16dbf5c2f343eaa9199163fb", expand=False, url="https://files.pythonhosted.org/packages/63/a8/e2929e8654c15a64504022a8bd1444e748a8bda3450a4868567caf19a6c1/category_encoders-2.8.0-py3-none-any.whl")
	version("2.8.1", sha256="ba77bde0a0afe13732b04997635b1ae82569e42c9696bc361c68674197988303", expand=False, url="https://files.pythonhosted.org/packages/92/fb/908cb215a30b117bb079a767176038599a5447f2506e21aa2e90d0aabfff/category_encoders-2.8.1-py3-none-any.whl")

	depends_on("py-setuptools", type=("build"))
	depends_on("python@3.10:", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-pandas", type=("build", "run"))
	depends_on("py-patsy", type=("build", "run"))
	depends_on("py-scikit-learn", type=("build", "run"))
	depends_on("py-scipy", type=("build", "run"))
	depends_on("py-statsmodels", type=("build", "run"))

# {'numpy(>=1.8.0)': ['1.2.7', '1.2.8'], 'scipy(>=0.9)': ['1.2.7', '1.2.8'], 'pandas(>=0.15.0)': ['1.2.7', '1.2.8'], 'scikit-learn(>=0.15.0)': ['1.2.7', '1.2.8'], 'statsmodels(<=0.8.0,>=0.6.0)': ['1.2.7', '1.2.8'], 'patsy(>=0.4.0)': ['1.2.7', '1.2.8'], 'numpy(>=1.11.1)': ['1.3.0'], 'scikit-learn(>=0.17.1)': ['1.3.0'], 'scipy(>=0.17.0)': ['1.3.0'], 'statsmodels(>=0.6.1)': ['1.3.0', '2.0.0', '2.1.0'], 'pandas(>=0.20.1)': ['1.3.0'], 'patsy(>=0.4.1)': ['1.3.0', '2.0.0', '2.1.0'], 'numpy(>=1.11.3)': ['2.0.0', '2.1.0'], 'scikit-learn(>=0.20.0)': ['2.0.0', '2.1.0', '2.2.2', '2.3.0', '2.4.0', '2.4.1', '2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1'], 'scipy(>=0.19.0)': ['2.0.0', '2.1.0'], 'pandas(>=0.21.1)': ['2.0.0', '2.1.0', '2.2.2', '2.3.0', '2.4.0', '2.4.1'], 'numpy(>=1.14.0)': ['2.2.2', '2.3.0', '2.4.0', '2.4.1', '2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1', '2.7.0', '2.8.0', '2.8.1'], 'scipy(>=1.0.0)': ['2.2.2', '2.3.0', '2.4.0', '2.4.1', '2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1', '2.7.0', '2.8.0', '2.8.1'], 'statsmodels(>=0.9.0)': ['2.2.2', '2.3.0', '2.4.0', '2.4.1', '2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1', '2.7.0', '2.8.0', '2.8.1'], 'patsy(>=0.5.1)': ['2.2.2', '2.3.0', '2.4.0', '2.4.1', '2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1', '2.7.0', '2.8.0', '2.8.1'], 'pandas(>=1.0.5)': ['2.5.0', '2.5.1', '2.5.1.post0', '2.6.0', '2.6.1', '2.7.0', '2.8.0', '2.8.1'], 'numpy>=1.14.0': ['2.6.2', '2.6.3', '2.6.4'], 'scikit-learn>=0.20.0': ['2.6.2', '2.6.3', '2.6.4'], 'scipy>=1.0.0': ['2.6.2', '2.6.3', '2.6.4'], 'statsmodels>=0.9.0': ['2.6.2', '2.6.3', '2.6.4'], 'pandas>=1.0.5': ['2.6.2', '2.6.3', '2.6.4'], 'patsy>=0.5.1': ['2.6.2', '2.6.3', '2.6.4'], 'importlib-resources;python_version<"3.9"': ['2.6.2', '2.6.3', '2.6.4'], 'scikit-learn(>=1.0.0,<1.6.0)': ['2.7.0'], 'scikit-learn(>=1.6.0)': ['2.8.0', '2.8.1']}