.. URLs-checker documentation master file, created by
   sphinx-quickstart on Thu Mar 19 22:18:12 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to URLs-checker's documentation!
========================================
*URLs-checker* :
A GitHub action to collect and check URLs in a project (code and documentation).
The action aims at detecting and reporting broken links.

.. raw:: html

  <p><a href="https://travis-ci.org/urlstechie/URLs-checker" rel="nofollow"><img src="https://camo.githubusercontent.com/d55441a84ff4b8580cf651ea809341b59c779670/68747470733a2f2f7472617669732d63692e6f72672f75726c737465636869652f55524c732d636865636b65722e7376673f6272616e63683d6d6173746572" alt="Build Status" data-canonical-src="https://travis-ci.org/urlstechie/URLs-checker.svg?branch=master" style="max-width:100%;"></a>
  <a href="https://codecov.io/gh/urlstechie/URLs-checker" rel="nofollow"><img src="https://camo.githubusercontent.com/16cd980babdb5facac453d3caf3ad381ce50c673/68747470733a2f2f636f6465636f762e696f2f67682f75726c737465636869652f55524c732d636865636b65722f6272616e63682f6d61737465722f67726170682f62616467652e737667" alt="codecov" data-canonical-src="https://codecov.io/gh/urlstechie/URLs-checker/branch/master/graph/badge.svg" style="max-width:100%;"></a>
  <a href="https://github.com/marketplace/actions/urls-checker"><img src="https://camo.githubusercontent.com/2279990b8ec4c43d3d77eaa327827c0635147a4e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d61726b6574706c6163652d55524c732d2d636865636b65722d626c75653f6c6f676f3d646174613a696d6167652f706e673b6261736536342c6956424f5277304b47676f414141414e5355684555674141414134414141414f4341594141414166534333524141414142484e4353565149434167496641686b6941414141416c7753466c7a4141414d36774141444f734235645a453067414141426c30525668305532396d64486468636d5541643364334c6d6c7561334e6a5958426c4c6d39795a35767550426f41414145525355524256436952685a472f53734d7846455a506673564a36316a62786146306352515263524a39686c596e333049484e2f2b3969717544434f4973626c49724f6a714b677935614b6f4a516a344f33454574625077684a62723654653238436d64534b65717a6571723059626656497254424b616b76744f6c356474546b4b2b76344866413950457942464359394147566743424c614270316a50417966414a2f41416449454730644e41697950372b4b317149664d646f6e5a6963362b574a6f424a76516c7675774471635861645575715041314e4b416c657862525441494d764d4f436a54624d776c314c74492f364b574a3551367254364874314d413538415838417063717174357232716872674158514333435a3669312b4b4d6439545275334d76413361482f6646506e426f6462366f6536484d382b6c5948724764525857384d39624d5a745058556a6936396c6d6635436d616d713771754e4c465a5844395271377630427063316f2f74703066697341414141415355564f524b35435949493d" alt="GitHub Marketplace" data-canonical-src="https://img.shields.io/badge/Marketplace-URLs--checker-blue?logo=data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAA4AAAAOCAYAAAAfSC3RAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAM6wAADOsB5dZE0gAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAAERSURBVCiRhZG/SsMxFEZPfsVJ61jbxaF0cRQRcRJ9hlYn30IHN/+9iquDCOIsblIrOjqKgy5aKoJQj4O3EEtbPwhJbr6Te28CmdSKeqzeqr0YbfVIrTBKakvtOl5dtTkK+v4HfA9PEyBFCY9AGVgCBLaBp1jPAyfAJ/AAdIEG0dNAiyP7+K1qIfMdonZic6+WJoBJvQlvuwDqcXadUuqPA1NKAlexbRTAIMvMOCjTbMwl1LtI/6KWJ5Q6rT6Ht1MA58AX8Apcqqt5r2qhrgAXQC3CZ6i1+KMd9TRu3MvA3aH/fFPnBodb6oe6HM8+lYHrGdRXW8M9bMZtPXUji69lmf5Cmamq7quNLFZXD9Rq7v0Bpc1o/tp0fisAAAAASUVORK5CYII=" style="max-width:100%;"></a>
  <a href="https://www.python.org/doc/versions/" rel="nofollow"><img src="https://camo.githubusercontent.com/521d61b5225b6d3d4081752be7ff5779e8c3a87e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e35253230253743253230332e36253230253743253230332e372d626c7565" alt="Python" data-canonical-src="https://img.shields.io/badge/python-3.5%20%7C%203.6%20%7C%203.7-blue" style="max-width:100%;"></a>
  <a href="https://github.com/SuperKogito/URLs-checker/blob/master/LICENSE"><img src="https://camo.githubusercontent.com/07a231564afff314fd36b9a0276216c988f5baae/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c6963656e73652d4d49542d627269676874677265656e" alt="License" data-canonical-src="https://img.shields.io/badge/license-MIT-brightgreen" style="max-width:100%;"></a>
  <a href="https://www.codefactor.io/repository/github/urlstechie/urls-checker" rel="nofollow"><img src="https://camo.githubusercontent.com/149af239e516b222b4386173749fe6051d0bb1b8/68747470733a2f2f7777772e636f6465666163746f722e696f2f7265706f7369746f72792f6769746875622f75726c737465636869652f75726c732d636865636b65722f6261646765" alt="CodeFactor" data-canonical-src="https://www.codefactor.io/repository/github/urlstechie/urls-checker/badge" style="max-width:100%;"></a></p>


Documentation
===============

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   check
   fileproc
   urlproc


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
