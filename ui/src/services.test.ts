import axios, { AxiosStatic } from 'axios';
import moxios from 'moxios'

import settings from "./settings";
import { isLoggedIn, login, logout } from "./services";

describe("services", () => {
  describe("isLoggedIn function", () => {
    beforeEach(function () {
      moxios.install()
    })

    afterEach(function () {
      moxios.uninstall()
    })

    describe("when user is logged out", () => {
      it("isLoggedIn returns false", async () => {
        moxios.wait(function () {
          let request = moxios.requests.mostRecent()
          request.respondWith({
            status: 403,
            response: {
              status: "failure",
              message: "The user is *NOT* authenticated."
            }
          }).then(function () {
            const result = isLoggedIn();
            expect(result).toBe(false)
          });
        })
      });
    });

    describe("when user is logged in", () => {
      it("isLoggedIn returns true", async () => {
        moxios.wait(function () {
          let request = moxios.requests.mostRecent()
          request.respondWith({
            status: 200,
            response: {
              status: "success",
              message: "The user is authenticated."
            }
          }).then(function () {
            const result = isLoggedIn();
            expect(result).toBe(false)
          });
        })
      });
    });
  });

  describe("login function", () => {
    const { location } = window;

    beforeAll(() => {
      delete window.location;
      window.location = { assign: jest.fn() };
    });

    afterAll(() => {
      window.location = location;
    });

    it("redirects the user to the login page (outside of react)", () => {
      login();
      expect(window.location.assign)
        .toHaveBeenCalledWith(settings.loginRedirectUri);
    });
  });
});
