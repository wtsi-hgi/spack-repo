# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PyDjangoCacheUrl(PythonPackage):
	"""Use Cache URLs in your Django application."""
	
	homepage = "https://github.com/epicserve/django-cache-url"
	pypi = "django-cache-url/django_cache_url-3.4.6-py2.py3-none-any.whl" 

	version("0.1", sha256="51e20da6453ab4e7019f21ca55929c272b5b02689ce4c6b2974f0f49a8459383", expand=False, url="https://files.pythonhosted.org/packages/90/0b/c37eeee036bab3aa62e01e979cb3c97fd14dcb86d7afb3f2f4597c88764d/django_cache_url-0.1-py2.py3-none-any.whl")
	version("0.2", sha256="1203c68ca38bff378b938a3f399f4dadb5b69c769bfb591b5aca7c575e6e4e5f", expand=False, url="https://files.pythonhosted.org/packages/6e/4e/dfc58df8107583bb6e030245692f5825d11ebd36905da44b9859b0bc7e44/django_cache_url-0.2-py2.py3-none-any.whl")
	version("0.2.1", sha256="c7e96e918095151d1afd012fc6ad9fadbb6b391878397f9d927e1203db0bc296")
	version("0.3", sha256="0622038c6d9239d814ee1dddf52585133cf7c61ceaec9cfcd01530f2af0d1bf7", expand=False, url="https://files.pythonhosted.org/packages/67/dc/6e2d6a507d9766468a8c91ed5de2c2f5c3ae616ce2b6f8d35d1214b03cc6/django_cache_url-0.3-py2.py3-none-any.whl")
	version("0.3.1", sha256="a032cff7a9fe9aa5179f582592a84bd0914f3cd7a528d8395e33aec58d1015e3", expand=False, url="https://files.pythonhosted.org/packages/5b/a5/07af8b185557a4e0c601150e35381ae7a8773b72bd386a26bfe32def4a03/django_cache_url-0.3.1-py2.py3-none-any.whl")
	version("0.3.2", sha256="096372e75bd5bfd9625108dd485cef29fb54a1895c123058cdc39428f1c243e6", expand=False, url="https://files.pythonhosted.org/packages/8b/28/eb37df7f362820340e4b85bd85bb669b74cf356ee0a6fbf38672f87bef20/django_cache_url-0.3.2-py2.py3-none-any.whl")
	version("0.3.3", sha256="d63e13e5da48daf66e1595d88ace40b3cbcb9f43053584ed5b2429ff0bac44bb", expand=False, url="https://files.pythonhosted.org/packages/4d/21/95306d238410ac80ea3818b64d1216bc150c7420d9e819934b1f744a9c20/django_cache_url-0.3.3-py2.py3-none-any.whl")
	version("0.3.4", sha256="d63dfe42fcdb06e4bc3ac016e65ff828d5da18ee7b4f9f00350fbda543f4dc95", expand=False, url="https://files.pythonhosted.org/packages/9d/cb/7f393dbb12cebf76d32ce5b6fc84791bc2e81d46519b8fa9d8b597c490d6/django_cache_url-0.3.4-py2.py3-none-any.whl")
	version("0.4.0", sha256="6541a00c921b05574531f0234cc004fe30c57086bb72276d03c93260ef001d0a", expand=False, url="https://files.pythonhosted.org/packages/db/1c/c37c1782138fc0dd14d0d0c45011ba66b78f351a819756068ddc5e06ccfb/django_cache_url-0.4.0-py2.py3-none-any.whl")
	version("0.5.0", sha256="37f979c65657f2c42412b5728b7393df80c137a4dddb1f00c93aed7ea7bc4882", expand=False, url="https://files.pythonhosted.org/packages/01/8e/a4745ff94a308f25dd04b6ecad3a4e151fc9175be102655eb2be5f50b3e0/django_cache_url-0.5.0-py2.py3-none-any.whl")
	version("0.6.0", sha256="be38f9bda7d6ac1dda63252136d69d90a2c8f28fdcdd7dabdc4ef16ab3881948", expand=False, url="https://files.pythonhosted.org/packages/6c/1a/178a4c287d4cb8f235a18a5e107a3a33c6ebd04649e80c34619150251397/django_cache_url-0.6.0-py2.py3-none-any.whl")
	version("0.7.0", sha256="0037107e27ab238f8261daf50a11114d87c5cbd2a7087819d2d6588b85d690af", expand=False, url="https://files.pythonhosted.org/packages/29/60/20aba1ffe40200c473a92138a997ac12688134d47f312d8f2d57dccd540c/django_cache_url-0.7.0-py2.py3-none-any.whl")
	version("0.8.0", sha256="b2c0b399c25588c2a19729f50398b30a8d279396b4449cacd07b34d20e2f52de", expand=False, url="https://files.pythonhosted.org/packages/11/32/acd2870244349d5c77abad93a3f70f7bc167ccff2472985d053e1bfa983d/django_cache_url-0.8.0-py2.py3-none-any.whl")
	version("1.0.0", sha256="71506c127aba566ab1b9b77bf09ccd3119a387aeb76df1b34f2541ce4764901c", expand=False, url="https://files.pythonhosted.org/packages/04/5d/d994bc364ad15a5ffb543cdc2c02e60550251634653dde3afe15a48c5268/django_cache_url-1.0.0-py2.py3-none-any.whl")
	version("1.1.0", sha256="37cc33c002c93f70c76b07d23ba4d49d9b955f44745c8c20a8d6b223558c0a27", expand=False, url="https://files.pythonhosted.org/packages/c8/86/6f3607810a199bd57a9c7e0e963df9db4887d83fbbf9cc625128d5de028c/django_cache_url-1.1.0-py2.py3-none-any.whl")
	version("1.2.0", sha256="94734964bc58394a5153bf03300ea7ea109fa317d23677e0d6d6913c079b3f29", expand=False, url="https://files.pythonhosted.org/packages/f4/7b/c9df452d457709fdccdcf7a34cdc46a91383a51ca71ebe929e97c158d005/django_cache_url-1.2.0-py2.py3-none-any.whl")
	version("1.3.0", sha256="ad84fc04f625bdbde3c937349f833925cab4b47a2cd824dd2a7ff5dbd98cc4ef", expand=False, url="https://files.pythonhosted.org/packages/85/68/a67ce60c283be1b31c4e084e6480af623f0982208b85bac707cedfe6a1f1/django_cache_url-1.3.0-py2.py3-none-any.whl")
	version("1.3.1", sha256="d0a8fce123ac35e397bf3b4528528df709a546780625a218794972c0ced77375", expand=False, url="https://files.pythonhosted.org/packages/63/27/5b37e81bce1fa9bafdc608d521c141bbddb32fefd72e7bae624b1afa9aa3/django_cache_url-1.3.1-py2.py3-none-any.whl")
	version("1.4.0", sha256="f3709cf9d1b474240ff304d56d28b8e5221d49b666ac1a07acabd98cdc413220", expand=False, url="https://files.pythonhosted.org/packages/09/48/375481af13515564e5bf5574a9f69d6c2e6b869e75946fb4093bcbbf179e/django_cache_url-1.4.0-py2.py3-none-any.whl")
	version("2.0.0", sha256="f0009452c4d63468714c7ff59266085947f3f3cc0947b3b2e87121bb27538d6c", expand=False, url="https://files.pythonhosted.org/packages/c3/0f/d18451ac43a5dca0f3939c660fc16792180dcc93aa0f9da827ab80b53a73/django_cache_url-2.0.0-py2.py3-none-any.whl")
	version("3.0.0", sha256="964120787dc80e568a355385a3880a19f2f00219c251903956f3137d1583d097", expand=False, url="https://files.pythonhosted.org/packages/75/7d/cb11e01b6c7089fd4ec8e3e24ec6b7490c1b1686ec0043d867e65e005fe3/django_cache_url-3.0.0-py2.py3-none-any.whl")
	version("3.1.0", sha256="edb584b37a70b5d1d5909ccc4a0d2f0239828757b6789df7f0f800d5f842a52a", expand=False, url="https://files.pythonhosted.org/packages/cb/b1/a7d40759bdb711c396190bfee53977bb457b744bab7aa1336367626e7ae3/django_cache_url-3.1.0-py2.py3-none-any.whl")
	version("3.1.1", sha256="04cac7f452ecbf4a88ce59fec8daaaa96fb5a81a0f2f6cbfa2fa9ce2de261c17", expand=False, url="https://files.pythonhosted.org/packages/20/17/e339c092ffeaea559ddd7857685f54de6958ed85849b6b828262cb89912d/django_cache_url-3.1.1-py2.py3-none-any.whl")
	version("3.1.2", sha256="889ac5d56105bdf44c0fd8f82c024119e198baf0bf698fdf49b1d5de92d8d4bb", expand=False, url="https://files.pythonhosted.org/packages/bb/4a/2997c01594412c8b740526adb717d327f24635bc8e830e54b3b969654b0c/django_cache_url-3.1.2-py2.py3-none-any.whl")
	version("3.2.2", sha256="f75a2e234c6541c5507cdb7c6c1b9f072643be4f3cadbb363dc34487fd6257a6", expand=False, url="https://files.pythonhosted.org/packages/3b/8f/fdcae4a19e6dc7ab31d21123493b0d34b148d19aa2ad8e7f1e9d5e4d18ab/django_cache_url-3.2.2-py2.py3-none-any.whl")
	version("3.2.3", sha256="5514ca3a2075c6b956b3d0a5c540654d32b004e76340d7bdabf6661135b5f218", expand=False, url="https://files.pythonhosted.org/packages/70/3f/c5195d948484f06edb687ef5978ec284a094839d0bd4a71a5eb394d820d6/django_cache_url-3.2.3-py2.py3-none-any.whl")
	version("3.3.0", sha256="dd689515d78a824f469d9cd4e447198999d2f13d1279487da20203f2f3b1e06b", expand=False, url="https://files.pythonhosted.org/packages/74/ad/78b14d495ca16865b6ad0cdcd7ec941feb2e3a839182ae599c8b86bdf4fc/django_cache_url-3.3.0-py2.py3-none-any.whl")
	version("3.4.0", sha256="9061f8e7ffbb29eb92ba93fa9058003ec92393e85c537d1969570652ff8721fa", expand=False, url="https://files.pythonhosted.org/packages/bd/17/d87dd15e3c5f3a96a72dc956780e0e4b08709f2af71ac6576519e63c9296/django_cache_url-3.4.0-py2.py3-none-any.whl")
	version("3.4.2", sha256="c4a62634cffc9d636073cef597a44576d67b07660ab2ef1f02b160ee7ecf0e98", expand=False, url="https://files.pythonhosted.org/packages/36/ad/3f0777fc12c04217e82692e6bd96a05cb69b6ff79d0ee506fca725d749d3/django_cache_url-3.4.2-py2.py3-none-any.whl")
	version("3.4.4", sha256="5ca4760b4580b80e41279bc60d1e5c16a822e4e462265faab0a330701bb0ef9a", expand=False, url="https://files.pythonhosted.org/packages/f9/e2/004e1fc61bda1f84f9e7e255987ed76c825122fc86e03752eca9711ec635/django_cache_url-3.4.4-py2.py3-none-any.whl")
	version("3.4.5", sha256="5f350759978483ab85dc0e3e17b3d53eed3394a28148f6bf0f53d11d0feb5b3c", expand=False, url="https://files.pythonhosted.org/packages/48/90/01755e4a42558b763f7021e9369aa6aa94c2ede7313deed56cb7483834ab/django_cache_url-3.4.5-py2.py3-none-any.whl")
	version("3.4.6", sha256="af524c2f47d753d3324a6a38a03ab8f6147b045c81cbb5ec2bfc8ecb9c95ed3c", expand=False, url="https://files.pythonhosted.org/packages/a2/80/3933edc478585103ab2726eacb0dd70aec60bc4c52208e427829b9700577/django_cache_url-3.4.6-py2.py3-none-any.whl")

