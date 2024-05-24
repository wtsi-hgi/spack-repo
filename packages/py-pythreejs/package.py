# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyPythreejs(PythonPackage):
	"""Interactive 3D graphics for the Jupyter Notebook and JupyterLab, using Three.js and Jupyter Widgets."""
	
	homepage = "https://github.com/jupyter-widgets/pythreejs"
	pypi = "pythreejs/pythreejs-2.4.2-py3-none-any.whl" 

	version("0.1.0", sha256="bd0a880ff07719f9eb159357d3cf5a0fa0f8238fb79e78518b4e14121a53fdbe")
	version("0.1.1", sha256="50775679babe0fa8a026c2f08be01ec6d67d57daba0072d33a5fb3ff1aea422c")
	version("0.1.12", sha256="1d58fd6466c4b9fac7d156312c5a8679d6bafbc1b41b81e82aaa1917004299ec")
	version("0.1.13", sha256="795b35eb58908708c57136c83de6f8a7fe82e279aa1a64cead7804cdbd759e1f")
	version("0.1.14", sha256="4e08cf8cbfad8572f3ba1fb9e629b3afc22366d8bf3bd8e2da3a05bcafdcc4fb")
	version("0.1.15", sha256="77269ea46b69bbe7280e47b98d2f12d382a4fc522080d9237fab71927514b8dc")
	version("0.1.16", sha256="4c20c68a31d97b272597327f6ac976b6cf4d6ee759a486ca4796aa9b3db3396d")
	version("0.1.17", sha256="7e6272661035a233d5f84893b3ee28f058bcc87cbb32afd3b93eacf0177e4ae8")
	version("0.1.18", sha256="14c7231e0fde132215975cd2638717d12da1797bcac33ee164ab2969e2eb7bb4")
	version("0.1.19", sha256="897d5da3ac9eeaf67b7a202e5eba74bac4ad45139adb03842b24fe1c4f522bf8")
	version("0.1.2", sha256="536cd40e8f17425ac8c6908e38e375bf3548070302e484dd01ed48b46b95d703")
	version("0.1.3", sha256="bcd8e29bae58b5fd86bc64b6a0127dc1b773bf6a3dc3e3131e0ce0f6bd63dbc9")
	version("0.1.4", sha256="4a0c1a283e7553abe6f7d2c17c8ede0168414b3ed7c72c9dd45a56e9caac260d")
	version("0.1.5", sha256="ab80034f8380a6d7181952c8bbf6a32d9ceac7b2ffdf25fd77086967fb219972")
	version("0.1.6", sha256="6878d8d9aa2e7957b1ca8d8c2749622e80f2135776aca207c7fe09fe3ec88cbe")
	version("0.1.7", sha256="a4f02d38c46002adb78e3b722585ffeb051a577880aa7eefb3457b74d196c5b3")
	version("0.2.0", sha256="bf0783e46a37a0138d1696e52ba627a2eb910d20b54fe28044a53b083cd3bb94", expand=False, url="https://files.pythonhosted.org/packages/39/b5/f4b26ab022fe43d59eac16151d1bc62a2bcfa9d095e8f990f9676aff1f58/pythreejs-0.2.0-py2.py3-none-any.whl")
	version("0.2.0b1", sha256="25e8bd22da4af1db40a14d045010864249a86bc56bcb9450e27c2bf6262f9b96", expand=False, url="https://files.pythonhosted.org/packages/20/3b/096516e4fd210fdf0001f4c296a647706f76623aa17cd5ef760ac71d267d/pythreejs-0.2.0b1-py2-none-any.whl")
	version("0.2.0b2", sha256="66f07988c531d8a86ebd905c979c92803585a8ff8920b917bbd7b78503ffd8fe", expand=False, url="https://files.pythonhosted.org/packages/e4/b5/c90d62d9bc66e57147a54ba4ed5af737db4fcb95732c9e132ce37d314a79/pythreejs-0.2.0b2-py2.py3-none-any.whl")
	version("0.2.1", sha256="f74e276ad9340973d59fc94c31d2f3a27787618369a624f2b4acaf6cb0f52f3e", expand=False, url="https://files.pythonhosted.org/packages/ca/ee/69250e15813a73f6bff66ec55e2669bc1f7e25db1c793ba3bafa8db21d9c/pythreejs-0.2.1-py2.py3-none-any.whl")
	version("0.2.2", sha256="1c9c4a035e3777e6bbdf2f19f918522231086732f2a47026fd7ec590345aa0a6", expand=False, url="https://files.pythonhosted.org/packages/27/52/31e2fb6a00208e767378dc82d6f4a5537b3ce12e0edff93b0cbac5915b77/pythreejs-0.2.2-py2.py3-none-any.whl")
	version("0.2.3", sha256="02407bfb4054c1b197f9e922fde0c1918cfbcc3ceeca71e7eca4a4910ab91d02", expand=False, url="https://files.pythonhosted.org/packages/45/a2/60efb7fa0fd16362f902101a3a40a3966f7bd0db664e17de8e4a8607af3d/pythreejs-0.2.3-py2.py3-none-any.whl")
	version("0.3.0", sha256="019f14fc808af4fe24d6a861850dc8d6e36626fb8759c12192f3b35fcedbdfea", expand=False, url="https://files.pythonhosted.org/packages/fc/dc/22d83068f282a308898608a20df4dc81b5fc5b509afbaea6d1e9b202d550/pythreejs-0.3.0-py2.py3-none-any.whl")
	version("0.3.1", sha256="2f26bfceefb3f11dbadc94303a397212c1bc62550ba7873e4d625dfa93903c3b", expand=False, url="https://files.pythonhosted.org/packages/5d/e5/666b8c26dc2de8da803cf79de50db61dbce36962ee4f58a8c9906cb36b6b/pythreejs-0.3.1-py2.py3-none-any.whl")
	version("0.4.0", sha256="2880a45b174c77f39a99f871c5eb8bab6b96c48ee2cfdfd2255680fe0bf46fda", expand=False, url="https://files.pythonhosted.org/packages/13/7d/719f980c383a90494942e508860bfa4131fbaed3ea669ba687cc5e02acb5/pythreejs-0.4.0-py2.py3-none-any.whl")
	version("0.4.0a0", sha256="ee11a89efcc55641cc2312d991b627cef595d37fdd1a3ee78eea1724e1161f41", expand=False, url="https://files.pythonhosted.org/packages/ab/c0/e062c4ae01445ac14acc0f955c203df3e84ccf03d083e7c815fc308deb23/pythreejs-0.4.0a0-py2.py3-none-any.whl")
	version("0.4.1", sha256="664a57b90f254773e4af7422026a05c618235585f362bc9429e710c9b551f2b0", expand=False, url="https://files.pythonhosted.org/packages/69/c2/1ca1ebbd62b353452ba94c7727f127031d5429ad0cb3b758e2b84f1b20ea/pythreejs-0.4.1-py2.py3-none-any.whl")
	version("1.0.0", sha256="706e2f0ddc09a8ba302b97ac9ef3eb442808411d707d495db10699b552fddd5e", expand=False, url="https://files.pythonhosted.org/packages/94/49/04c40cede42b49f11110296bbd134800ec540cc512a8fd2b77414849a6cc/pythreejs-1.0.0-py2.py3-none-any.whl")
	version("1.0.0b0", sha256="156ff3b0da6fa1557a4ef41cdf915eaec690725aba8e126a8730dc1fb6cd2425", expand=False, url="https://files.pythonhosted.org/packages/4d/62/017c7a0e0c3ab3fbbcaaf128f9e52a6c98f1a875822078254e8aa74ee63b/pythreejs-1.0.0b0-py2.py3-none-any.whl")
	version("1.0.0b2", sha256="8550563e033edf842cc60e5e2e1a08db6639dd0a877bd21a0ab18fcf4fe40b09", expand=False, url="https://files.pythonhosted.org/packages/d3/bf/dd0fc291c6c4b64d79d633c6d8b912b8ab7ba8dfbc373d6d262859886d1d/pythreejs-1.0.0b2-py2.py3-none-any.whl")
	version("1.0.0b3", sha256="a54776a8a3f85cf19688e62bba6c3db7366b2c5ed6b8884a178b2117329172dc", expand=False, url="https://files.pythonhosted.org/packages/0e/18/6ed3b4c7411c117d3e7b949ba7fdfd83a58616f0b4d832fa1e8c9881d8b0/pythreejs-1.0.0b3-py2.py3-none-any.whl")
	version("1.0.0b4", sha256="96ae4c3c4048d2feb951475d78431bcfded13ffed9b1262db1aad7676d6d788f", expand=False, url="https://files.pythonhosted.org/packages/76/d2/2155f291a890806197a6aa3ef2aee42d322ff40fc3d904bcc7ff56a2a6da/pythreejs-1.0.0b4-py2.py3-none-any.whl")
	version("1.0.0b5", sha256="dcf08a0eb3c72c4f014862146d441188112af7053fd198ce38addfa094b795c9", expand=False, url="https://files.pythonhosted.org/packages/be/dd/f307b6e8a538cc08adbb8c1a51d293ea1888c6076235a57705982db2d841/pythreejs-1.0.0b5-py2.py3-none-any.whl")
	version("1.0.0b6", sha256="2b76bf6a547793ee5c03574cc45ab04deeef29a4e4a0b5abe6373cf527523c06", expand=False, url="https://files.pythonhosted.org/packages/5a/78/5d9b74c1fc77af962458d9fccfe9442c36f37dd2efec8df86cdbf864afdb/pythreejs-1.0.0b6-py2.py3-none-any.whl")
	version("1.1.0", sha256="855971c9e76e12924d0a8df8843941d2e8f7947f23464e9c9290e2c9de9d98ca", expand=False, url="https://files.pythonhosted.org/packages/77/61/4c2f1b7752fb65c7ead7e64695c721a0ec324f8f1d8cb2ea965d874d3e62/pythreejs-1.1.0-py2.py3-none-any.whl")
	version("2.0.0", sha256="77cf878fb976e6211e879f85c4250795ee0228445bd9f96296808005d317e009", expand=False, url="https://files.pythonhosted.org/packages/5a/68/3378c3e6120f798fae075aff967b7ce3ff240b99537a574895f4058e10aa/pythreejs-2.0.0-py2.py3-none-any.whl")
	version("2.0.1", sha256="525ec05a9304b2ab6fe28635cc39359055c609fd8b928abe37f907a8926a15ee", expand=False, url="https://files.pythonhosted.org/packages/52/ec/3bff66fbb588240370a8c888c1b0fed64bde66d57a885776152c23a084a9/pythreejs-2.0.1-py2.py3-none-any.whl")
	version("2.0.2", sha256="30890efab6a6d71dc4290b37cdbb142a30602fb6c00e4e020dd030fa11031e70", expand=False, url="https://files.pythonhosted.org/packages/b6/0e/f6dbe6e1a9a489cca1bcada3ee0ae5fd49cfb123c6829cc9c1c6583a3fa8/pythreejs-2.0.2-py2.py3-none-any.whl")
	version("2.1.0", sha256="5915f30504aeeffb7d102444174186be8ed6216f4e226f5952d8573c95d52f84", expand=False, url="https://files.pythonhosted.org/packages/f9/9a/2593be7fed0b6bf4f854c4ca042ee94820ce1b005e9094ae319a540b798d/pythreejs-2.1.0-py2.py3-none-any.whl")
	version("2.1.1", sha256="aa11d7f2f6864b3c0491db0831d12396be284cfedb34a61fbe2bf8083f612924", expand=False, url="https://files.pythonhosted.org/packages/41/21/8307f7308686a08fa7be43ff5e25daf041c8b46d5874a243c262e4665cb8/pythreejs-2.1.1-py2.py3-none-any.whl")
	version("2.2.0", sha256="e2dcbe067b8c7f54240ee0330aeb8aef03edc43e92e5bcf9bdf0d158b4517bf6", expand=False, url="https://files.pythonhosted.org/packages/66/5b/15f1e42debee32a2f40e73786a789fea90cce3d177004a148fef5523b16e/pythreejs-2.2.0-py2.py3-none-any.whl")
	version("2.2.1", sha256="73dd43946c5c042a2fea8cfcdc6ddd6723c0d281c4fa9c9efd1ffde554ba6371", expand=False, url="https://files.pythonhosted.org/packages/85/8b/160380c438c9ab8a131734a9f441a790e47c3ba9802cfa098f6775b450fd/pythreejs-2.2.1-py2.py3-none-any.whl")
	version("2.3.0", sha256="d638f600d9a7322198caaad0c4d77d89b85e4272e0d340a6c0a3f3ceaf385ed4", expand=False, url="https://files.pythonhosted.org/packages/2e/36/806ac843a15c67b013dc85a4761d3cc8bfa08dab70fb3f63dbc6611a5809/pythreejs-2.3.0-py2.py3-none-any.whl")
	version("2.4.0", sha256="9d1e661a8dd7b5eef8a14617716180ac2bbe70b634c249394acc2564e52dcf33", expand=False, url="https://files.pythonhosted.org/packages/33/05/7e3e5f96a5387a26c1ff5da7a7a1cacd618097e52c0b2947da05a2434af5/pythreejs-2.4.0-py3-none-any.whl")
	version("2.4.1", sha256="a8a758b4519e56984ae42c7fae512020129d504569a096656c09f040889ed598", expand=False, url="https://files.pythonhosted.org/packages/08/49/e0208def3cb5c38c571941b64df5d4594326100370289ffc41f41992dd21/pythreejs-2.4.1-py3-none-any.whl")
	version("2.4.2", sha256="8418807163ad91f4df53b58c4e991b26214852a1236f28f1afeaadf99d095818", expand=False, url="https://files.pythonhosted.org/packages/d8/8b/e2bbeb42068f0c48899e8eddd34902afc0f7429d4d2a152d2dc2670dc661/pythreejs-2.4.2-py3-none-any.whl")

	depends_on("python@3.7:", type=("build", "run"))
	depends_on("py-traitlets", type=("build", "run"))
	depends_on("py-numpy", type=("build", "run"))
	depends_on("py-ipydatawidgets", type=("build", "run"))
	depends_on("py-ipywidgets", type=("build", "run"))
